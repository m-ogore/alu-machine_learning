#!/usr/bin/env python3

"""
Provides some stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient


if __name__ == "__main__":
    """
    Gets stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')

    db = client.logs

    collection = db.nginx
    
    total_logs =collection.count_documents({})
    
    print(f'{total_logs} logs')
    
    print('Methods:')
    
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    for method in methods:
        print(f'method {method}: {collection.count_documents({"method": method})}')

    print(f'{collection.count_documents({"method": "GET", "path": "/status"})} status check')
             #["count"]} status check')

