from django.urls import path

from . import views

app_name = 'basket'  # Same as namespace in core/urls.py

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
]