#!/usr/bin/env python3
import json
import requests
import time
import sys
import urllib3
from base64 import b64encode

def ClusterConnect():
    requests.packages.urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#  print 'Number of arguments:', len(sys.argv), 'arguments.'
#  print 'Argument List:', str(sys.argv)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#  base_url = "https://192.168.86.20:9440/api/nutanix/v3/"
    base_url = "https://10.59.98.253:9440/api/nutanix/v3/"

    s = requests.Session()
    s.auth=("epenedos","Nutanix/4u$")
    s.headers.update({'Content-Type': 'application/json'})
