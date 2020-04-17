import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input('Please enter the url: ')
html = urllib.request.urlopen(url)
sum = 0
data = html.read().decode()
tree = ET.fromstring(data)
result_list = tree.findall('comments/comment')
for results in result_list:
    sum +=int(results.find('count').text)
print(sum)