import requests
import json


resp = requests.get('https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&body=aiohttp&site=stackoverflow')
j = json.loads(resp.text)

for i in j['items']:
    title = i['title']
    link = i['link']
    print(title + ' (' + link + ')')