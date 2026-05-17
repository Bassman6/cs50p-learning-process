import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()
responds = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(responds.json(),indent = 2))

