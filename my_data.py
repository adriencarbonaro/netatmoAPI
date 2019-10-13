#!/usr/bin/env python3

import requests
import json

# -- Open .json file -----------------------------------------------------------
json_file = 'credentials.json'
with open(json_file, "r") as json_data:
    cred = json.load(json_data)

# -- Prepare API request -------------------------------------------------------
params = {
    'access_token'  : cred["access_token"],
    'device_id'    : '70:ee:50:13:67:ca'
}

try:
    # -- Send API request and get json response --------------------------------
    response = requests.post("https://api.netatmo.com/api/getstationsdata", params)
    response.raise_for_status()
    data = response.json()["body"]
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)


