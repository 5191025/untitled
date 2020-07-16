import lxml
import requests

URI = "https://www.hsc.ac.jp"
r = requests.get(URI)

root = lxml.html.fromstring(r.content)

print(root.cssselect('a'))
