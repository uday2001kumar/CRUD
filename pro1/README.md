
This is a simple CRU (Create, Read, Update) application built using [Python,Django,DRF].

# Features

- Create new Products
- View list of Products
- Update existing Products

# Setup instructions
1. Go to the Below URL
    https://github.com/uday2001kumar/CRUD

2. Download the zip file and extract it.

3. Open terminal and create virtual Environment.

    i. python -m venv env_name

    ii.  cd env_name

    iii. cd scripts

    iv activate

4. After activating the environment goto project directory(pro1).
5. Install the requirements.

   pip install django djangorestframework numpy pandas openpyxl

6. run the following commands

    python manage.py makemigrations

    python manage.py migrate

    python manage.py createsuperuser

        username: Enter your username

        email: Enter your email
        
        password: Enter your password

        confirm password: Enter confirm password

# Run Guidence
1. To run the project

    python manage.py runserver

2. Copy URL http://127.0.0.1:8000/

3. Goto the Browser and past it.
    we can see the follwing URL Patterns
    admin/
    api/
    
    http://127.0.0.1:8000/admin 
    -> then it will ask username and password. After login we can access the admin interface.
    -> we can add,update and delete the categories and products.

    http://127.0.0.1:8000/api/
    -> we can see the following URL patterns.

        api/ add_category/
        api/ list_categories/
        api/ add_product/
        api/ list_products/
        api/ update_product/<int:pk>/
        api/ upload_file/

        here all the urls open in the postman
        =====================================
        1. Open the postman
        2. Paste that cooresponding URL 
        3. Select that corresponding method(GET,POST,PUT,DELETE,PATCH)
        4. Enter the key name and correspoding value.

        http://127.0.0.1:8000/api/add_category/
        -> Add the category.(POST method)
        

        http://127.0.0.1:8000/api/list_categories/
        -> we can see the list of Categories.(GET method)

        http://127.0.0.1:8000/api/add_product/
        -> Add the Product.(POST method)

        http://127.0.0.1:8000/api/list_products/
        -> We can see the list products.(GET method)

        http://127.0.0.1:8000/api/update_product/product_id/
        -> We can update the product details.(PUT method)

        http://127.0.0.1:8000/api/upload_file/
        -> We can upload the excel file.(POST method)

        








