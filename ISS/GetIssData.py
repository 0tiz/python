#!/usr/bin/env python3

import urllib.request
import json
from datetime import datetime



def IssData(IssApi):
    response = urllib.request.urlopen(IssApi)
    obj = json.loads(response.read())
    getCheckOnline = obj['message']
    getLongitude = obj['iss_position']['longitude']
    getLatitude = obj['iss_position']['latitude']
    getIssDateAndTime = datetime.utcfromtimestamp((int(obj['timestamp']))).strftime('%Y-%m-%d %H:%M:%S')


    pass
# if  check == 'success':





