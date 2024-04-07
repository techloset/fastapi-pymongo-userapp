from bson import ObjectId
from fastapi import FastAPI
import uvicorn
from config.db import db_connect
from dotenv import load_dotenv
from pydantic import BaseModel
# from pymongo import ObjectId

load_dotenv()
app = FastAPI()
db = db_connect()
users = db["users"]


class Users(BaseModel):
    name: str
    email: str
    phone: str


@app.get("/")
def routeMethod():
    return "Server is up and running.."


@app.post("/users")
def create_user(user: Users):
    try:
      userRecord = user.dict()
      users.insert_one(userRecord)
      print(userRecord)
      return "user created successfully"
    except Exception as e:
      print(e)
      return "Something went wrong"


@app.delete("/users/{id}")
def delete_user(id):
      try:
          users.delete_one({"_id": ObjectId(id)})
          return "user deleted successfully"
      except Exception as e:
        print(e)
        

@app.put("/users/{id}")
def update_user(id, user: Users):
    try:
      userRecord = user.dict()
      users.update_one({"_id":ObjectId(id)},{"$set":userRecord})
      return "user updated successfully"
    except Exception as e:
      print(e)
      return "Something went wrong"
    



@app.get("/users")
def get_users():
    try:
        usersData = users.find()
        usersRecord = []
        for user in usersData:
            user["_id"] = str(user["_id"])
            usersRecord.append(user)
        return usersRecord
      
    except Exception as e:
      print(e)
    
@app.get("/users/{id}")
def get_users(id:str):
    try:
        usersData = users.find({"_id":ObjectId(id)})
        usersRecord = []
        for user in usersData:
            user["_id"] = str(user["_id"])
            usersRecord.append(user)
        return usersRecord
      
    except Exception as e:
      print(e)
    

def start():
    uvicorn.run("students.main:app",host="127.0.0.1", port=8080, reload=True)
