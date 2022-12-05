#!/usr/bin/env python
"""
main.py: *Caution* need API Key, Private Key, JSON Web Token(JWT)
"""

__author__      = "DongKyu Lee"
__copyright__   = "Copyright 2022, Dong Kyu Lee"
__email__		= "dev.dongklee@gmail.com"


import gzip
import requests, time, json
from authlib.jose import jwt

URL_DEST = "https://api.appstoreconnect.apple.com/v1/salesReports"
KEY_NAME = ""
KEY_ID = ""
ISSUER_ID = ""
PATH_TO_KEY = ""
EXPIRATION_TIME = round(time.time() + 20 * 60)
# IN_HOUSE = False

with open(PATH_TO_KEY, 'r') as f:
	PRIVATE_KEY = f.read()

jwt_header = {
	"alg": "ES256",
	"kid": KEY_ID,
	"typ": "JWT"
}

jwt_payload = {
	"iss": ISSUER_ID,
	"exp": EXPIRATION_TIME,
	"aud": "appstoreconnect-v1"
}
api_params = {
	'filter[frequency]':'YEARLY',
	'filter[reportDate]':'2021',
	'filter[reportType]': 'SALES',
	'filter[reportSubType]': 'SUMMARY',
   'filter[vendorNumber]': '86659758'
}

# Generate Token
jwt_token = jwt.encode(jwt_header, jwt_payload, PRIVATE_KEY)

# Generate Request
api_auth = 'Bearer ' + jwt_token.decode()
api_url = URL_DEST
api_header = {'Authorization': api_auth}

try:
	api_req = requests.get(api_url, params=api_params, headers=api_header)	#params={'limit': 200}
except Exception as e:
	print(e)

file_content = gzip.decompress(api_req.content).decode('utf-8')

# TODO:: More Detail
print(file_content)
