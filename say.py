"""import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])"""

#requests
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
