# Ecommerce_Django
Ecommerce is project for student assignment using django (Python)

## Django Setup
To set up Django for your project, follow these steps:

1. Make sure you have Python installed on your system. You can check by running the following command in your terminal:

    ```bash
    python --version
    ```

    If Python is not installed, you can download it from the official Python website: https://www.python.org/downloads/

2. Install Django using pip, which is the package installer for Python. Run the following command in your terminal:

    ```bash
    pip install django
    ```

    This will install the latest version of Django.

3. Create a new Django project by running the following command in your terminal:

    ```bash
    django-admin startproject project_name
    ```

    Replace `project_name` with the desired name for your project.

4. Change into the project directory by running the following command:

    ```bash
    cd project_name
    ```

5. Run the development server to verify that your Django installation is working correctly:

    ```bash
    python manage.py runserver
    ```

    This will start the development server on `http://localhost:8000/`. You should see a "Congratulations!" message in your browser.

Congratulations! You have successfully set up Django for your project.

# Run in docker

    # Install docker in Window

    To install Docker in Windows , you can follow these steps:

        1. Go to the Docker website (https://www.docker.com/products/docker-desktop) and download Docker Desktop for Windows.

        2. Run the installer and follow the on-screen instructions to complete the installation.

        3. Once the installation is complete, Docker Desktop will be running in the background.

        4. You can verify the installation by opening a command prompt or PowerShell window and running the following command:

            ```
            docker --version
            ```

            If Docker is installed correctly, you should see the version number displayed.

        5. You can now use Docker to run containers and manage your development environment.

    To install Docker in Mac, you can follow these steps:

    1. Go to the Docker website (https://www.docker.com/products/docker-desktop) and download Docker Desktop for Mac.
    2. Run the installer and follow the on-screen instructions to complete the installation.
    3. Once the installation is complete, Docker Desktop will be running in the background.
    4. You can verify the installation by opening a terminal window and running the following command:

        ```
        docker --version
        ```
        If Docker is installed correctly, you should see the version number displayed.
    5. You can now use Docker to run containers and manage your development environment.

    # Build Image (Docker Compose)
    docker-compose build

    # Run Image
    docker-compose up


![alt text](static/images/list_product_screen.png)