import requests
import json

r = requests.get('https://wiki.xn--rckteqa2e.com/')
text = r.text
number = text.split('#mw-content-text > div > table.bluetable.c.sortable.jquery-tablesorter > tbody > tr:nth-child(1)')



print(number)