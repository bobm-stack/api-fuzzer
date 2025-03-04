import requests
import sys 

api = input("please enter the ip of the api:" ) 

def fuzzer():
  for word in sys.stdin:
    discover = requests.get(url= api + f"/{word}")
    if discover.status_code == 404:
      fuzzer()
    else:
      discovered = discover.json()
      print(discovered)
  
