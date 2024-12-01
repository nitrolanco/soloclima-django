from pymongo import MongoClient
from django.conf import settings


def get_mongo_collection():
    """
    Connect to MongoDB and return the Productos collection.
    """
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DBNAME]
    return db["Productos"]


def fetch_all_products():
    """
    Fetch all products from the Productos collection.
    """
    collection = get_mongo_collection()
    products = list(collection.find({}, {"_id": 0}))  # Exclude the MongoDB ObjectID
    return products
