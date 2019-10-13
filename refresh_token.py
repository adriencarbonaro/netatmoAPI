#!/usr/bin/env python3

import requests
import json

# -- Open .json file -----------------------------------------------------------
json_file = 'credentials.json'
with open(json_file, "r") as json_data:
    cred = json.load(json_data)

# -- Prepare API request -------------------------------------------------------
payload = {
    'grant_type'    : 'refresh_token',
    'refresh_token' : cred["refresh_token"],
    'client_id'     : cred["client_id"],
    'client_secret' : cred["client_secret"]
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
    print("--------------------------------------------------------------------------")
    print("Updating credentials.json file ... ", end=" ")

    # -- Write new tokens to credentials file ----------------------------------
    cred["access_token"] = access_token
    cred["refresh"]      = refresh_token

    with open(json_file, "w") as json_data:
        json.dump(cred, json_data)

    print("Done")

except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)

