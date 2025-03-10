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
    print(response)

poke_name = "pikachu"
get_info(poke_name) 
