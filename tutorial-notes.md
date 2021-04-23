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
    * Created tests for models
4. URL's, Views
    * Create url paths
    * Create home page view
    * Create categories view function and made available to all views
    * Create detail page for product

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
1:36:29