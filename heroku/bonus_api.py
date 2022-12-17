import requests
import json
url = "https://data.mongodb-api.com/app/data-aktxk/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "rates",
    "database": "forex",
    "dataSource": "finalproject",
    "projection": {
        "_id": ' '
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'HuZN3LRNuxgM4nqsplVYFqfZt7akC5svVUcjryHdmdpmsmVLQgjNgJQRPR5YxrJS', 
}



response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)