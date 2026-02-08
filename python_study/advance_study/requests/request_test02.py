# @Author: Benanahai
# @Time  : 2024/11/17 22:04

import requests
from django.contrib.gis.geos.prototypes.threadsafe import GEOSFunc

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(f"cookies: {r.cookies}")
print(f"text: {r.text}")


