#!/usr/bin/env python3
import json
import requests
import time
import sys
import urllib3
from base64 import b64encode

class nutanixapi:

    def __init__(self):
        self.clusterIP=""

    def clusterConnect(self,clusterIP,userid,passwd):
        self.ntxclusterip=clusterIP
        self.ntxuser=userid
        self.ntxpasswd=passwd
        requests.packages.urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.base_url = "https://" + self.ntxclusterip + ":9440/api/nutanix/v3/"

        s = requests.Session()
        s.auth=(userid,passwd)
        s.headers.update({'Content-Type': 'application/json'})

    def listClusters(self):
        body_cluster = {"kind": "cluster"}
        r = self.s.request("POST",self.base_url + 'cluster/list/' + catname, data=json.dumps(body_cluster),verify=False)
        return r
