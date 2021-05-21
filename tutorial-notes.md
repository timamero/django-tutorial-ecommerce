# Notes
Notes while following tutorial

## Part 1
1. Getting started with Django
2. Models & Admin
    * Created Category and Product models
    * Added MEDIA_ROOT settings to settings.py and urls.py to allow images
    * Registered model to admin site
3. Testing Models
    * Used coverage to see what needs to be tested
    * Build tests for models
4. URL's, Views
    * Create url paths
    * Create home page view
    * Create categories view function and made available to all views
    * Create detail page for product
    * Create dynamic links (get_absolute_url)
    * Create category page
    * Build Test for Views
5. PEP 8 Python Style Guide
    * Reviewed guidelines

### Part 1 Notes
[Code Repository](https://github.com/veryacademy/YT_Django_Project_Ecommerce_v1_Part1)
* db_index (field option): If True, a database index will be created for this field
    * [What is indexing?](https://dataschool.com/sql-optimization/how-indexing-works/)
* slug: slug is the unique identifying part of a web address, typically at end of the URL
* [What is `related_name` used for in Django?](https://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django)
* [Model.Admin.prepopulated_fields](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields)
* [ModelAdmin.list_editable](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_editable)
* [Coverage](https://coverage.readthedocs.io/en/coverage-5.5/)
* Testing
    * Install coverage
    ```
    pip install coverage
    ```
    * Run tests under coverage
    ```
    coverage run manage.py tests
    ```
    * To only run only tests in application use omit
    ```
    coverage run --omit='*/venv/*' manage.py test
    ```
    * Report on results
    ```
    coverage report
    ```
    * For a presentation of report, get HTML
    ```
    coverage html
    ```
* Django appends `_id` to the end of the foreign field category name in the database
* [HTTP reponse status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
* [RequestFactory](https://docs.djangoproject.com/en/3.2/topics/testing/advanced/) (Django Advanced testing topic)
    * Used for testing views as function instead of through Client browser
* [Flake8](https://pypi.org/project/flake8/) (Source code checker)
    * PEP 8 style guide enforcement
    * To install: `pip install flake8`
    * Create file `setup.cfg` in same directory as manage.py
    * Include the following in the file
        ```
        [flake8]
        exclude = .git, *migrations*, *venv*
        max-line-length = 119
        ```
    * To run: `flake8`
    * To check and automatically order library imports, install isort package: `pip install flake8-isort`
    * To run isort: `isort`


## Part 2
1. Refactoring
    * Create custom context_processors
    * Create model managers
    * Update names
    * Add default image
    * Add tests
2. Introducing Sessions
    * Learn about sessions
    * Learn about AJAX
    * Learn how to decode session data
3. Development:
        * Created new app called basket
        * Set up url and first view called basket_summary
        * Create basket link in navigation
        * Create basket class in basket.py
    1. Add to basket
    2. Delete from basket
    3. Update basket

    
4. Testing

### Part 2 Notes
* [Code Repository](https://github.com/veryacademy/django-ecommerce-project/tree/main/Part-02%20Build%20an%20E-commerce%20Basket%20with%20Sessions)
* [Writing your own context processors](https://docs.djangoproject.com/en/3.2/ref/templates/api/#writing-your-own-context-processors)
    * Created `context_processors.py` in `store` folder
    * Added the following to `context_processors.py`
        ```
        from .models import Category


        def categories(request):
            """To make available in all views, add 'store.views.categories' to TEMPLPATES.OPTIONS.context_processors"""
            return {
                'categories': Category.objects.all()
            }
        ```
    * In `settings.py`, update the categories context processor
        ```
         'store.context_processors.categories'
         ```
    * Delete the previous context processor in `views.py`
* [Managers](https://docs.djangoproject.com/en/3.2/topics/db/managers/)
    * Instead of `products = Product.objects.filter(is_active)` in `views.py`, can use `products = Product.products.all()` instead and filter the object in the model Manager
    * In `models.py` add the following:
        ```
        class ProductManager(models.Manager):
            def get_queryset(self):
                return super(ProductManager, self).get_queryset().filter(is_active=True)

        class Product(models.Model):
            ...
            objects = models.Manager()
            products = ProductManager()
        ```
    * This keeps the `views.py` file small and makes the models do most of the work which is favorable.
* Default image should be included so that you don't force user to upload image and to use default image if there is a problem with the image
    * Update `image` field in `Product` model
    ```
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    ```
* When you deploy application to server, need to update `ALLOWED_HOSTS` in settings.  Change this before production
    ```
    ALLOWED_HOSTS = ['yourdomain.com', '127.0.0.1']
    ```
* Setting up static files
    * Create static folder at root of project folder (same location as core folder)
    * In `settings.py`, the static settings should be:
    ```
    STATIC_URL = '/static/'

    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    ```
    * This tells Django where the static files are placed
* Need jQuery for AJAX
    * Get CDN at [https://code.jquery.com/](https://code.jquery.com/)
* Sessions
    * Session is temporary and interactive information
    * Single user per session - save retrieve arbitrary data on a per-site-visitor basis
    * Store the data server side
    * User receives a session ID which is stored in cookie in the browser
        * Session ID is only made on page refresh or redirect
    * Session ID is used to retrieve the associated data
    * AJAX (Asynchronous JavaScript and XML) can be used to update session data without refreshing page
        * AJAX would be saving changes in page, should match page when page is refreshed
    * In Django, session data is stored in django_session table
        * Fields: session_key, session_data, expire_date
    * Can decode session_data:
        * Open shell
        ```
        py manage.py shell
        ```
        * Import Session model
        ```
        from django.contrib.sessions.models import Session
        * Run get with session_key
        ```
        s = Session.objects.get(pk='ra4x41ux1iw178h9kzpfa9aij6ds8ujs')
        ```
        * Use get_decode to decode session data
        ```
        s.get_decoded()
        ```
    * Can set up expire_date to occur at any time you want
    * Can view session data in browser by opening developer tools and going to Application tab
* Basket will be created as new app to compartamentalize functionality
    * Remember to add app to INSTALLED_APPS in settings.py and add url mapping
1:31:48