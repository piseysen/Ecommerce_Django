from math import ceil
from django.shortcuts import render, redirect
from ecommerceapp.models import Contact, Product, Orders, OrderUpdate
from django.contrib import messages

# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values("category", "id")
    print(catprods)
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    
    params = {"allProds": allProds}
    
    
    return render(request, "index.html", params)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        phonenumber = request.POST.get("phonenumber")
        print(name, email, desc, phonenumber)
        contact = Contact(name=name, email=email, desc=desc, phonenumber=phonenumber)
        contact.save()
        messages.info(request, "we will get back to you soon.")
        
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You need to login first and then try again.")
        return redirect("/auth/login")
    
    
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt', '')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        
        # check if items_json is empty
        if items_json == "":
            messages.warning(request, "Your cart is empty. Please add items to your cart.")
            return redirect("index")
        else:
            Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
            print(amount)
            Order.save()
            
            # generate oid ex: 1ShopyCart
            Order.oid = str(Order.order_id) + "ShopyCart"
            Order.amountpaid = amount
            Order.paymentstatus = "PAID"
            Order.save()
            
            
            update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
            update.save()
            thank = True
            messages.success(request, "Your order has been placed successfully.")
            id = Order.order_id
            return render(request, "checkout.html", {"thank": thank, "id": id})
    
    return render(request, "checkout.html")


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You need to login first and then try again.")
        return redirect("/auth/login")
    currentuser = request.user.username
    items = Orders.objects.filter(email=currentuser)
    # prevent the items is empty
    if len(items) == 0:
        messages.warning(request, "You have not placed any orders yet.")
        return redirect("index")
    else:
        print(items)
        rid = ""
        for i in items:
            print(i.oid)
            myid = i.oid
            rid = myid.replace("ShopyCart", "")
            print(rid)
        print(rid)
        status = OrderUpdate.objects.filter(order_id=int(rid))
        print(status)
        context = {
            "items": items,
            "status": status
        }
    
    return render(request, "profile.html", context)

# custom 404 view
def error_404(request, exception):
    return render(request, '404.html', status=404)
