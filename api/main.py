from typing import Optional
import mysql.connector
from fastapi import FastAPI
import json

mydb = mysql.connector.connect(
    host="deeplift-database.cugzfo4s5ndw.us-east-1.rds.amazonaws.com",
    user="deeplifter123",
    password="j4capstone2021",
    port="3306",
    database="deeplift"
)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users")
def read_item():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM DeepliftUser")
    myresult = mycursor.fetchall()
    res = []
    for user in myresult:
        res.append(user)
    return res

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
