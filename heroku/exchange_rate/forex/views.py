from django.shortcuts import  render
# from forex.models import Forex
from pymongo import MongoClient
from datetime import datetime

# import requests

def connect_():
    uri = "mongodb+srv://admin:admin12345@forex.np4kinx.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    print(client)
    db = client.forex
    collection = db['rates']
    print(collection,"Collection")
    return collection

from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


# def get_rates(request):
#     print(request)
#     # date_today = datetime.now().strftime("%Y-%m-%d")
#     # collection.find({"date": date_today})
#     # return collection
#     # return render (request, 'forex/forex.html', { "all_rates": all_rates} )

import collections


# Heroku app is also up and running but for some reason it is not showing our output..
def get_rates(request, date):
    print('get_rates')
    data = list(connect_().find({"date": date}))
    print(data[0]['date'])
    sorted_exchange_rates = dict(sorted(data[0]['rates'].items(), key=lambda item: item[1]))
    # print(sorted_exchange_rates, "*"*10)
    bottom_5 = take(5, sorted_exchange_rates.items())
    # print(bottom_5, "bottom")
    # bottom_5_keys = list(sorted_exchange_rates)[-5:]
    reversed_dict = collections.OrderedDict(reversed(list(sorted_exchange_rates.items())))
    top_5 = take(5, reversed_dict.items())
    # for key in bottom_5_keys:
    # print(top_5, "top 5"*5)

    # print(list(sorted_exchange_rates)[-5:], "last")
    # result = dict(tuples)

    # printing the result
    # print(result)



    # for key in data[0]['rates'].keys():
    max_value_key = max(data[0]['rates'], key=data[0]['rates'].get)
    print(max_value_key) 
    min_value_key = min(data[0]['rates'], key=data[0]['rates'].get)
    print(min_value_key)   

    # sorted_value = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}

    return render (
        request,
        'forex/rate_detail.html',
        {'date': data[0]['date'],
        'rates': data[0]['rates'],
        'max' :  data[0]['rates'][max_value_key],
        'min' :  data[0]['rates'][min_value_key],
        'top_5' : dict(top_5),
        'bottom_5' : dict(bottom_5),
        # 'sorted' : data[0][sorted_value]
        }
    )