# products/views.py
from django.http import JsonResponse
from pymongo import MongoClient
from django.conf import settings
from django.shortcuts import render


def get_products(request):
    # Connect to MongoDB
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DBNAME]
    collection = db["Productos"]

    # Query the database
    products = list(collection.find({}, {"_id": 0}))  # Exclude the MongoDB ObjectId

    # Add pagination and search functionality
    search_query = request.GET.get("search", "")
    if search_query:
        products = [
            product
            for product in products
            if search_query.lower() in product.get("name", "").lower()
        ]

    # Pagination setup
    page = int(request.GET.get("page", 1))
    items_per_page = 10
    start = (page - 1) * items_per_page
    end = start + items_per_page

    paginated_products = products[start:end]

    return JsonResponse(paginated_products, safe=False)


def get_product_detail(request, product_id):
    # Connect to MongoDB
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DBNAME]
    collection = db["Productos"]

    # Query the database for the product
    product = collection.find_one({"id": product_id}, {"_id": 0})

    if not product:
        return JsonResponse({"error": "Product not found"}, status=404)

    return JsonResponse(product, safe=False)


def product_list(request):
    # Connect to MongoDB
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DBNAME]
    collection = db["Productos"]

    # Query the database
    products = list(collection.find({}, {"_id": 0}))  # Exclude the MongoDB ObjectId
    # Rename '_id' to string for template rendering

    # Render the product_list.html template with the products
    return render(request, "product_list.html", {"products": products})
