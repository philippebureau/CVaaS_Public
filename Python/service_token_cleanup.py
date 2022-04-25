#!/usr/bin/python
import requests
import os
import datetime

#disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Setting environment variable from file
with open('/mnt/hgfs/Ubuntu_shared/cvaas.tok', 'r') as file:
    token_data = file.read().rstrip()
os.environ['GNMI_TOKEN'] = token_data


GNMI_TOKEN = os.getenv('GNMI_TOKEN')
cookies = {
    'access_token': f"{GNMI_TOKEN}",
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
data = '{"partialEqFilter":[{"user":"Phil"}]}'

response = requests.post('https://www.arista.io/api/v3/services/arista.serviceaccount.v1.TokenService/GetAll', headers=headers, cookies=cookies, data=data, verify=False)
json_data = response.json()

current_time = datetime.datetime.utcnow().isoformat()

for value in json_data:
    key_id = value['value']['key']['id']
    expiration = value['value']['valid_until']
    if current_time > expiration:
        print("token " + key_id + " is expired and will be deleted")
        token_id = f'{{"key":{{"id":"{key_id}"}}}}'
        response = requests.post('https://www.arista.io/api/v3/services/arista.serviceaccount.v1.TokenConfigService/Delete', headers=headers, cookies=cookies, data=token_id, verify=False)
    else:
        print("token " + key_id + " is still valid")
