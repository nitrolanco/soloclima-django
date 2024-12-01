from django.urls import path
from . import views

urlpatterns = [
    path(
        "products/", views.get_products, name="get_products"
    ),  # REST-like endpoint for products
]
