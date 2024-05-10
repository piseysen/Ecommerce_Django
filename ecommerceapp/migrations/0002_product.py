# Generated by Django 5.0.5 on 2024-05-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                ("product_name", models.CharField(max_length=100)),
                ("category", models.CharField(default="", max_length=100)),
                ("subcategory", models.CharField(default="", max_length=50)),
                ("price", models.IntegerField(default=0)),
                ("desc", models.CharField(max_length=300)),
                ("image", models.ImageField(default="", upload_to="images/images")),
            ],
        ),
    ]
