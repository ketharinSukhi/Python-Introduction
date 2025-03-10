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
# Using jeson in API

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
    print(f"{poke_info['name']}")
    
