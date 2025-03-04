import requests
import sys 

api = input("please enter the ip of the api:" ) 

for word in sys.stdin:
  discover = requests.get(url= api + f"/{word}")
  discovered = discover.json()
  print(discovered)
  
