# import sys
# import requests
# import json

# if len(sys.argv) != 2:
#     sys.exit()
# responds = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(responds.json(),indent = 2))


a = input("user input:")
import emoji
print(emoji.demojize("python is ::",language = "zh"))
print(emoji.emojize(f"python is :{a}:",language = "alias"))

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

# print(emoji.emojize('Python is :thumbsup:', language='alias'))

