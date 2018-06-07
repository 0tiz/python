## Version Python 2.7

import urllib2
import json

url_abfrage = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(url_abfrage)

obj = json.loads(response.read())
check = obj['message']
laengengrad = obj['iss_position']['longitude']
breitengrad = obj['iss_position']['latitude']


if  check == 'success':
    print 'erfolg'
else:
    print 'ISS ist down'



print obj['timestamp']
print 'ISS Laengengrad: '+laengengrad
print 'ISS Breitengrad: '+breitengrad
