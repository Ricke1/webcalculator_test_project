import requests
import json

args = {"x": int(1), "y": int(1)}

IP = '127.0.0.1'
PORT = '17678'
r = requests.get(f"http://{IP}:{PORT}/api/state")
print(r.json())

p = requests.post(f"http://{IP}:{PORT}/api/remainder", json = args)
info = p.json()

what = int(info['result'])

print(what)

print(1//1)


