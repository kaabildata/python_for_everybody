import json
import urllib.request, urllib.parse, urllib.error

sum = 0
url = input('Please enter the url: ')
html = urllib.request.urlopen(url)


data = html.read().decode()
data_dict = (json.loads(data))['comments']
for i in data_dict:
    sum +=i['count']

print(sum)