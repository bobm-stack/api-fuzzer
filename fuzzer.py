import requests
import sys 

api = input("please enter the ip of the api:" ) 

for word in sys.stdin:
  discover = requests.get(url= api + f"/{word}")
  if discover.status_code == 404:
    loop()
  else:
    discovered = discover.json()
    print(discovered)
  
