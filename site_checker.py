# Import Libraries
import time
import sys
import requests
from pushover import init, Client

# Import Variables & Secrets
from api_secrets import *
from sites import site_list

# Initialize Pushover
pushoverClient = Client(pushover_user_key, api_token=pushover_api_token)

for i in site_list:
    r = requests.get(i)
    if r.status_code == requests.codes.ok:
        print (r.url, r.status_code)
    else:
        print (r.url, r.status_code)
        pushoverClient.send_message("The url " + r.url + " failed to resolve. Error code: " + str(r.status_code))
       
print("Exiting in 3 seconds...")
time.sleep(3)
sys.exit()