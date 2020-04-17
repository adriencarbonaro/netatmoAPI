#!/usr/bin/env python3

import requests
import json

# -- Open credentials file -------------------------------------------------------------
json_file  = 'credentials.json'
json_const = 'constants.json'
with open(json_file) as json_data:
    cred = json.load(json_data)
with open(json_const, "r") as json_constants:
    const = json.load(json_constants)

# -- Prepare API request -------------------------------------------------------
# TODO: Get Coordinates from Geocoding API
# (Google Geocoding API, https://www.gps-coordinates.net/api, etc.)
params = {
    'access_token'  : cred["access_token"],
    'lat_ne'        : const["coordinates"]["lat_ne"],
    'lon_ne'        : const["coordinates"]["lon_ne"],
    'lat_sw'        : const["coordinates"]["lat_sw"],
    'lon_sw'        : const["coordinates"]["lon_sw"],
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


