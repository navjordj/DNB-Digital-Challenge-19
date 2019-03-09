import urllib.request
import json

import os
from dotenv import load_dotenv

from requests import get

load_dotenv()
token = os.getenv("TOKEN")

print(token)

def get_info():

    ip = get('https://api.ipify.org').text
    api = 'http://api.ipstack.com/' + ip + '?access_key=' + token
    #api = 'http://api.ipstack.com/134.201.250.155?access_key=779ef6e34d3eefce5dad592d0a97fe96'
    print(api)
    result = urllib.request.urlopen(api).read()
    result = result.decode()
    result = json.loads(result)

    return result #return dict

if __name__ == "__main__":
    print(get_info())