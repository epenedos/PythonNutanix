#!/usr/bin/env python3
import json
import requests

import time

def main():
	requests.packages.urllib3.disable_warnings()
	base_url = "https://192.168.1.123:9440/api/nutanix/v0.8/"
	s = requests.Session()
	s.auth=("admin","sdxsolutions")
	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})

	data = s.get(base_url + 'vms', verify=False).json()
	
	

	#myvm = {'numVcpus': 1,'memoryMb': 1024,'name': 'teste1234','vmNics': [{'networkUuid': '23cac028-9847-4cff-8b49-0192ecd49d26'}]}
	myMaster = "22219efc-8c49-49ed-be99-04eddf33ffb6"
	
	
	for n in range(1,400):
		vmName = "User"+str(n)
		myClone = {"specList": [{"name": "teste","vmNics": [{"networkUuid": "0c3f083e-6055-49d9-8bb9-b35b1b8217c3"}]}]}
		for name, datalist in myClone.items():
			for datadict in datalist:
				for key, value in datadict.items():
					if value == "teste":
						datadict[key] = vmName
		
		data = json.dumps(myClone)
		r = s.post(base_url + 'vms/' + myMaster + '/clone', data)
		result = r.json()
		print ('Clonning the VM ' + vmName)
#		time.sleep(1)
#		task = s.get(base_url + 'tasks/' + result["taskUuid"])
#		rtask = task.json()
#
#		print (rtask)

#		for e in rtask["entityList"]:
#			print ('Power on the VM ' + vmName)
#			power = s.post(base_url + 'vms/' + e["uuid"] + '/power_op/on',json.dumps({}))
#			rpower= power.json()
#			print (rpower)


if __name__ == "__main__":
  main()
