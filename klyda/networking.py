import requests, etc
from parsing import args
from bs4 import BeautifulSoup

def validate(): # checks if targeted url is online
    try:
        r = requests.get(args.url, timeout=args.timeout)
        if r.status_code == 200:
            return True
    except:
        return False

def sendreq(data): # sends request to target url
    r = requests.post(args.url, data=data, timeout=args.timeout)
    soup = BeautifulSoup(r.content , 'html.parser')
    etc.requests +=1
    return r.status_code, len(soup), soup