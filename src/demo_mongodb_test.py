import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["users"]
myuser = { "name": "Bob", "e-mail": "bobsmith@bob.com" }

print(myclient.list_database_names())
print(mydb.list_collection_names())
