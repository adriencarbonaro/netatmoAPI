#!/usr/bin/env python3

import requests
import json

# -- Open .json file ----------------------------------------
json_file = 'credentials.json'
with open(json_file) as json_data:
    cred = json.load(json_data)

# -- Prepare API request -------------------------------------------------------
payload = {
    'grant_type'    : "password",
    'username'      : cred["email"],
    'password'      : cred["password"],
    'client_id'     : cred["client_id"],
    'client_secret' : cred["client_secret"],
    'scope'         : cred["scope"]
}

try:
    # -- Send API request and get json response --------------------------------
    response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
    response.raise_for_status()
    access_token  = response.json()["access_token"]
    refresh_token = response.json()["refresh_token"]
    expires       = response.json()["expires_in"]
    scope         = response.json()["scope"]

    print("")
    print("Access token  : ", access_token)
    print("Refresh token : ", refresh_token)
    print("Scope         : ", scope)
    print("Expires in    : ", expires)

except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)

