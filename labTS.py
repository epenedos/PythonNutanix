#!/usr/bin/env python3
import json
import requests
import time

def main():
	requests.packages.urllib3.disable_warnings()
	base_url = 'https://10.68.69.102:9440/api/nutanix/v2.0/'
	s = requests.Session()
	s.auth=('admin','Ntnx.911')
	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})

	data = s.get(base_url + 'vms', verify=False).json()
	for e in data['entities']:
		vmUuid = e['uuid']
		vmName=e['name']
		print(vmName)
		
	
	
	createvm_json = json.dumps({"description":"TEAM6","guest_os":"win server 2012r2","memory_mb":4098,"name":"TEAM6","num_cores_per_ vcpu":1,"num_vcpus":1,"vm_disks":[{"disk_address":{"device_bus":"ide","device_index":0} ,"is_cdrom":True,"is_empty":False,"vm_disk_clone":{"disk_address":{"vmdisk_uuid":"d3e19aee-9926-4109-808e-ac18884b8d2f" }}},{"disk_address":{"device_bus":"scsi","device_index":0},"vm_disk_create":{"storage_container_uuid":"1fe71c49-1890-49e6-86d4-faebffdf45ae","size":50000000000}}]," hypervisor_type":"ACROPOLIS"})
	
	r = s.post(base_url + "vms/", data=createvm_json)
	print (r.json)
	
	
	time.sleep(10)
	
	data = s.get(base_url + 'vms', verify=False).json()
	for e in data['entities']:
		if e['name'].find('TEAM6') == 0:
			vmUuid = e['uuid']
			print ('Power On VM ' + vmName + ' ' + vmUuid) 
			power = s.post(base_url + 'vms/' + vmUuid + '/set_power_state/',json.dumps({"transition":"ON"}))
			
	time.sleep(20)
	
	r = s.delete(base_url + 'vms/' + vmUuid)
	
	
	
	
	
	
	
if __name__ == "__main__":
  main()
