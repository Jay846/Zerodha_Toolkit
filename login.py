from kiteconnect import KiteConnect
import datetime, json, os, sys

# Load stored API credentials
try:
    with open("Login Credentials.json", "r") as f:
        login_credential = json.load(f)
except:
    login_credential = {"api_key": input("API Key: "), "api_secret": input("API Secret: ")}
    if input("Press Y to save login credentials: ").upper() == "Y":
        with open("Login Credentials.json", "w") as f:
            json.dump(login_credential, f)

# Generate or load access token
if os.path.exists(f"AccessToken/{datetime.datetime.now().date()}.json"):
    with open(f"AccessToken/{datetime.datetime.now().date()}.json", "r") as f:
        access_token = json.load(f)
else:
    kite = KiteConnect(api_key=login_credential["api_key"])
    print("Login URL:", kite.login_url())
    request_token = input("Paste request token from URL: ")
    access_token = kite.generate_session(request_token, login_credential["api_secret"])['access_token']
    os.makedirs("AccessToken", exist_ok=True)
    with open(f"AccessToken/{datetime.datetime.now().date()}.json", "w") as f:
        json.dump(access_token, f)
