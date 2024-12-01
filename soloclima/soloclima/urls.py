from django.urls import path
from products.views import get_products, product_list, get_product_detail

urlpatterns = [
    path("api/products/", get_products, name="get_products"),
    path("products/", product_list, name="product_list"),  # Added product list page
    path(
        "api/products/<str:product_id>/", get_product_detail, name="get_product_detail"
    ),
]
