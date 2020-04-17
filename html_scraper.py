from urllib.request 
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url).read().decode()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all ofclear the anchor tags
tags = soup('h3')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)