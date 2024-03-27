import requests 
from data_input import dat_in
URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": dat_in}
r = requests.get(URL,headers=headers, json=data) 
r.json()