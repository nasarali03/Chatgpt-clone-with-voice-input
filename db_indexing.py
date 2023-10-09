import pymongo

# Establish a connection to your MongoDB server
client = pymongo.MongoClient("mongo_uri")  # Replace with your MongoDB server URL
db = client["chatgpt"]  # Replace with your database name
db.chats.create_index([("email",pymongo.ASCENDING)])