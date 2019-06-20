#!/usr/bin/env python3
import json 
import requests
import time
import sys


 
def main(argv):
  requests.packages.urllib3.disable_warnings()
  print 'Number of arguments:', len(sys.argv), 'arguments.'
  print 'Argument List:', str(sys.argv)
  base_url_acropolis = "https://192.168.1.200:9440/api/nutanix/v0.8/"
  base_url_NOS = "https://192.168.1.200:9440/api/nutanix/v0.8/"
  
  s = requests.Session()
  s.auth=("admin","sdxsolutions")
  s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
 

 
  net = {'vmid':'0c6d60c3-25c9-4e34-9722-55350e407275'}
  r = s.post(base_url + 'networks', data=json.dumps(net))
  
  result = r.json()
  	r = s.delete(base_url_acropolis + 'vms/'+'0c6d60c3-25c9-4e34-9722-55350e407275')
  
  result = r.json()
    
  print (result)
 
  
  
if __name__ == "__main__":
  main(sys.argv[1:])
