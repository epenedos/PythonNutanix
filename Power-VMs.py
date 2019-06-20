
import json
import requests
import time

def main():
	requests.packages.urllib3.disable_warnings()
	base_url = "https://172.27.108.20:9440/api/nutanix/v0.8/"
	s = requests.Session()
	s.auth=('admin','!Invers1s')
	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})

	data = s.get(base_url + 'vms', verify=False).json()
	print(data)
	for e in data['entities']:
		vmUuid = e['uuid']
		vmConfig = e['config']
		vmName=vmConfig['name']
		if vmName.find('NEWVM-1') == 0:
			print ('Power On VM ' + vmName + ' ' + vmUuid) 
			power = s.post(base_url + 'vms/' + vmUuid + '/power_op/off',json.dumps({}))
			rpower= power.json()
			time.sleep(0.5)


if __name__ == "__main__":
  main()
