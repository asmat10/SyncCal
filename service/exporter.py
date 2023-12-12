from pymongo import MongoClient

class MongoDBReader:
    def __init__(self, connection_uri, database_name, collection_name):
        self.client = MongoClient(connection_uri)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def read_all_entries(self):
        entries = self.collection.find()
        for entry in entries:
            print(entry)

if __name__ == "__main__":
    # Beispielverwendung der Klasse
    reader = MongoDBReader(
        connection_uri="mongodb+srv://admin:admin@cluster0.7mczdvg.mongodb.net/?retryWrites=true&w=majority",
        database_name="SyncCalDB",
        collection_name="SyncCalCollection"
    )

    reader.read_all_entries()


