
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import json

h = []
p = []
url = 'https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')

s = soup.find('h3')
temp = []
for elem in s.next_siblings:
    if elem.name == 'h3':
        h.append(elem.text)
        p.append(temp)
        temp = []
    else:
        temp.append(elem)

print(h)
# print(len(p))
#
# print(p)
final = {}
for val in h:
    final[val.split()[1]] = ' '.join(val.split()[2:])
Json_value = json.dumps(final)
print(Json_value)

with open("Scraped_data.json", "w") as outfile:
    outfile.write(Json_value)
