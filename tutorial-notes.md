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
2. Introducing Sessions
3. Development:
    1. Add to basket
    2. Delete from basket
    3. Update basket
4. Testing

### Part 2 Notes
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