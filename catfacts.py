import requests
import json
import urllib3

urllib3.disable_warnings()

def retrieveCatfact():
    cat = requests.get('https://catfact.ninja/fact?max_length=150',verify=False)
    
    fact = json.loads(cat.text)
    return fact['fact']

if __name__=='__main__':
    print(retrieveCatfact())