#!/usr/bin/env python3

import requests
import json

# -- Open credentials file -------------------------------------------------------------
json_file = 'credentials.json'
with open(json_file) as json_data:
    cred = json.load(json_data)

# -- Prepare API request -------------------------------------------------------
# TODO: Get Coordinates from Geocoding API
# (Google Geocoding API, https://www.gps-coordinates.net/api, etc.)
params = {
    'access_token'  : cred["access_token"],
    'lat_ne'        : 3,
    'lon_ne'        : 4,
    'lat_sw'        : -2,
    'lon_sw'        : -2,
    'required_data' : 'temperature',
    'filter'        : 'true',
}

try:
    # -- Send API request and get json response --------------------------------
    response = requests.post("https://api.netatmo.com/api/getpublicdata", params=params)
    response.raise_for_status()
    data = response.json()["body"]
    print(data[0])
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)


