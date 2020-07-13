""" 
    Title: mongodb_test.py
    Author: Professor Krasso
    Date: 10 July 2020
    Description: Test program for connecting to a 
                 MongoDB Atlas cluster
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# show the connected collections 
print("\n -- Pytech COllection List --")
print(db.list_collection_names())

# show an exit message
input("\n\n  End of program, press any key to exit... ")
