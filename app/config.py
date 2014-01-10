import json
from pprint import pprint
json_data=open('config.json')

data = json.load(json_data)
pprint(data)
print data["SqlData"]["usr"]
print data["SqlData"]["pwd"]
json_data.close()
