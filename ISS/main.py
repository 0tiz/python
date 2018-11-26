#!/usr/bin/env python3

import urllib.request
import json
import pprint

response = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")

obj = json.loads(response.read())
check = obj['message']
laengengrad = obj['iss_position']['longitude']
breitengrad = obj['iss_position']['latitude']


if  check == 'success':
    print ('erfolg')
else:
    print ('ISS ist down')



print (obj['timestamp'])
print ('ISS Laengengrad: '+laengengrad)
print ('ISS Breitengrad: '+breitengrad)
