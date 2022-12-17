import requests
from pprint import pprint
from pymongo import MongoClient
from datetime import datetime


def get_rates():
    print("HEYYY")
    resp = {}
    url = 'https://api.exchangerate.host/latest'

    response = requests.get(url)
    print(response)
    data = response.json()
    resp['date'] = data['date']
    resp['base'] = data['base']   
    resp['rates'] =  data['rates']
    # print(data)
    return resp
# get_rates()


def connect_():
    uri = "mongodb+srv://admin:admin12345@forex.np4kinx.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    print(client)
    db = client.forex
    print("***", db)
    collection = db['rates']
    # print(collection, "Collectiionnnnnnnnnnnnnnnnnnnn \n")
    return collection


def upload_data():
    print("upload")
    data = get_rates()
    # print(data)
    collection = connect_()
    date_today = datetime.now().strftime("%Y-%m-%d")
    # resp = collection.find({"date":date_today})
    if data['date'] == date_today:
        print(data['date'], "DATEEEEEEEEEE")
        collection.insert_one(data)
        print(data['date'], "DATE 2", collection)



upload_data()
def print_date():
    with open('try', '+w') as f:
        f.write("Try1")

print_date()