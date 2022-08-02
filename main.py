import selenium
import requests
import json


param_request = {'x': 4, 'y': 2}

IP = '127.0.0.1'
PORT = '17678'


r = requests.get(f"http://{IP}:{PORT}/api/state", params=param_request)
print(r.json())

