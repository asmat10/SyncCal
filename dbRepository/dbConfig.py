import pymongo
from pymongo import MongoClient

# Verbindung zur lokalen MongoDB auf Standardport (27017) herstellen
# client = MongoClient('localhost', 27017)

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://admin:admin@cluster0.7mczdvg.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print(client.list_database_names())
except Exception as e:
    print(e)
