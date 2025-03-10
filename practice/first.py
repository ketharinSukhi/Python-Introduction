"""name = str(input("What is your name? \n"))

if str.isalpha(name):
 print("my name is", name)
else:
 print("enter name")"""

"""def select(b):
    print(f"my name is {b}")
    
def main():
    x = str(input("what is your name ? "))
    select(x)
   
main()"""



"""import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])"""

import requests
base_url="https://pokeapi.co/api/v2/"

def get_info(name):
    url =f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        poke_data = response.json() #using jeson method we'll covert it to a python dictionary it will consist of key value pairs much like a jason file
        return poke_data
    else:
        print(f"Failed to retrieve data{response.status_code}")
        

poke_name = "pikachu"
poke_info = get_info(poke_name) 

if poke_info:
    print(f"{poke_info["name"]}")
    
