import requests
import json
# import google.oauth2.credentials
# from google.oauth2 import OAuth2WebServerFlow
import google_auth_oauthlib.flow
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

import json
# Use the client_secret.json file to identify the application requesting
# authorization. The client ID (from that file) and access scopes are required.
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'gmail_api_cred2.json',
    scopes=['https://mail.google.com/'])
# Indicate where the API server will redirect the user after the user completes
# the authorization flow. The redirect URI is required. The value must exactly
# match one of the authorized redirect URIs for the OAuth 2.0 client, which you
# configured in the API Console. If this value doesn't match an authorized URI,
# you will get a 'redirect_uri_mismatch' error.
flow.redirect_uri = 'http://localhost'


# Generate URL for request to Google's OAuth 2.0 server.
# Use kwargs to set optional request parameters.
authorization_url, state = flow.authorization_url(
    # Enable offline access so that you can refresh an access token without
    # re-prompting the user for permission. Recommended for web server apps.
    access_type='offline',
   # prompt = 'none',
    login_hint= 'services.iiitkare@gmail.com',
    # Enable incremental authorization. Recommended as a best practice.
    include_granted_scopes='true')
print(authorization_url)
# Ask the user to enter the authorization code
code = input('Enter the authorization code: ')

# Exchange the authorization code for an access token and refresh token
data = {"code":code,
        "client_id":"XXXXXXX",
        "client_secret":"XXXXXXX",
        "redirect_uri":"http://localhost",
        "grant_type":"authorization_code"}

response = requests.post("https://oauth2.googleapis.com/token", data=data)

# Save the token.json
with open("token.json", "w") as f:
    json.dump(response.json(), f)
