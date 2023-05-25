# Dependencies
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from flask import Flask, request, jsonify
from waitress import serve
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

import pymongo
# from pymongo.mongo_client import MongoClient

# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


uri = "mongodb+srv://ajitgupta:ajitgupta@cluster0.fmasiqv.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = pymongo.MongoClient(uri)
mydb = client["PRISM"]
mycol = mydb["AP"]

# Send a ping to confirm a successful connection


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print(data)
            print("Pinged your deployment. You successfully connected to MongoDB!")


            x = mycol.insert_one(data).inserted_id
            print(x)
            return {"status": "success"}
        except Exception as e:
            print(e)
            return {"status": "failed"}


@app.route('/')
def home():
    return "Hello"
   
if __name__ == "__main__":
    serve(app, host='0.0.0.0',port=8889,threads=2)
