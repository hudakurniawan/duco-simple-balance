#simple duco balance check
import requests
import json
import datetime

server = 'https://server.duinocoin.com/users/'
ts = datetime.datetime.now()

user = input('Duco-id : ')

#GET data
data = requests.get(server+user)
load = json.loads(data.content)
balance = load['result']['balance']['balance']

print(ts,balance)
