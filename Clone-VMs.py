
import json
import requests

import time

def main():
	requests.packages.urllib3.disable_warnings()
	base_url = "https://192.168.1.110:9440/api/nutanix/v0.8/"
	s = requests.Session()
	s.auth=("admin","!nutanix")

	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})

	data = s.get(base_url + 'vms', verify=False).json()
	
	myMaster = "651f727d-7487-4288-9c12-511f5bbbefc9" # MyCentos DR

	vlan = 100
	for n in range(1,100):
	
		
		vmName = "Web-" + str(n)
		
		myClone = {"specList": [{"name": "teste","vmNics": [{"networkUuid": "e3b31942-f8b0-49fa-b303-478b596e7687"}],"overrideNetworkConfig": True}]} 
		
		
		for name, datalist in myClone.items():
			for datadict in datalist:
				for key, value in datadict.items():
					if value == "teste":
						datadict[key] = vmName

												
		
		data = json.dumps(myClone)
		#print (data)
		r = s.post(base_url + 'vms/' + myMaster + '/clone', data)
		result = r.json()
		print ('Clonning the VM ' + vmName)
		time.sleep(0.5)


if __name__ == "__main__":
  main()