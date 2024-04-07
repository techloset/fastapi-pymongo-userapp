from pymongo import MongoClient
import os

def db_connect():
    try:
      uri = os.getenv("URI")
      client = MongoClient(uri)
      db = client["myapp"]
      return db
      
    except Exception as e:
        print(e)
      