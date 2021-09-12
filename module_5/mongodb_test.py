from pymongo import MongoClient 
import certifi

# MongoDB connection string
url ="mongodb+srv://admin:admin@cluster0.hyosd.mongodb.net/pytech"

# Connect to MongoDB Cluster
client = MongoClient(url,tlsCAFile=certifi.where())

# Connect pytech database
db = client.pytech

# Display the connected collections
print("\n -- Pytech Collection List --")
print(db.list_collection_names())

# Display end of program message
input("\n\n End of program, press any key to exit... ")
