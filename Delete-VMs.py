
import json
import requests

import time

def main():
	requests.packages.urllib3.disable_warnings()
	base_url = "https://192.168.1.110:9440/api/nutanix/v0.8/"
	s = requests.Session()
	s.auth=('admin','!nutanix')
	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})

	data = s.get(base_url + 'vms', verify=False).json()
	for e in data['entities']:
		vmUuid = e['uuid']
		vmConfig = e['config']
		vmName=vmConfig['name']
		if vmName.find('Web-') == 0:
			print ('Deleting VM ' + vmName + ' ' + vmUuid) 
			r = s.delete(base_url + 'vms/' + vmUuid)
			
		time.sleep(0.5)

if __name__ == "__main__":
  main()
