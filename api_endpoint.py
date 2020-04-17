import urllib.request, urllib.parse, urllib.error

import json

place_name = input("Enter a place name: ")
base_url = "http://py4e-data.dr-chuck.net/json?"
parms = dict()
parms['address'] = place_name
parms['key'] = 42
address_param =base_url+urllib.parse.urlencode(parms)
print(address_param)
connection = urllib.request.urlopen(address_param)

raw_data = connection.read().decode()
print ("Retrieved {0} characters".format(len(raw_data)))
parsed_data = json.loads(raw_data)

print ("Place id", parsed_data["results"][0]["place_id"])