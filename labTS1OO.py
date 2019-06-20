#!/usr/bin/env python3
import json
import requests
import time
import http.client



requests.packages.urllib3.disable_warnings()




def login():
	slack("TESTING")
	global base_url 
	base_url= 'https://10.21.5.37:9440/api/nutanix/v2.0/'
	global s
	s = requests.Session()
	s.auth=('admin','nx2Tech323!')
	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
	global vmUuid
	
	
	

def listVM():
	print(base_url)
	data = s.get(base_url + 'volume_groups', verify=False).json()
	for e in data['entities']:
		vmUuid = e['uuid']
		vmName=e['name']
		print (vmName)
		
	
def createVM():	
	createvm_json = json.dumps({"description":"TEAM6","guest_os":"win server 2012r2","memory_mb":4098,"name":"TEAM6","num_cores_per_ vcpu":1,"num_vcpus":1,"vm_disks":[{"disk_address":{"device_bus":"ide","device_index":0} ,"is_cdrom":True,"is_empty":False,"vm_disk_clone":{"disk_address":{"vmdisk_uuid":"d3e19aee-9926-4109-808e-ac18884b8d2f" }}},{"disk_address":{"device_bus":"scsi","device_index":0},"vm_disk_create":{"storage_container_uuid":"1fe71c49-1890-49e6-86d4-faebffdf45ae","size":50000000000}}]," hypervisor_type":"ACROPOLIS"})
	
	r = s.post(base_url + "vms/", data=createvm_json)
	print("Vm Created ---- See Prism")

def powerONVM():	
	data = s.get(base_url + 'vms', verify=False).json()
	for e in data['entities']:
		vmName=e['name']
		if vmName.find('TEAM6') == 0:	
			vmUuid = e['uuid']
			print ('Power On VM ' + vmName + ' ' + vmUuid) 
			power = s.post(base_url + 'vms/' + vmUuid + '/set_power_state/',json.dumps({"transition":"ON"}))
			
def deleteVM():	
	data = s.get(base_url + 'vms', verify=False).json()
	for e in data['entities']:
		vmName=e['name']
		if vmName.find('TEAM6') == 0:
			vmUuid = e['uuid']
			r = s.delete(base_url + 'vms/' + vmUuid)
			print ('Delete VM ' + vmName + ' ' + vmUuid) 


def loopy():	
	while 1:
		print("1-listvm")
		print("2-create VM")
		print("3-power on VM")
		print("4-Delete VM")
	
		opt = input("choose an option ")
		
		if opt == "1":
			listVM()
			
		if opt == "2":
			createVM()
			
		if opt == "3":	
			powerONVM()
		
		if opt == "4":	
			deleteVM()
		if opt == 5:
			break;


def slack(msg):

	uri = "https://hooks.slack.com/services/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"
	json_payload = {"text": msg}
	requests.post(uri, json=json_payload)
	s1 = requests.Session()
	s1.headers.update({'Content-Type': 'application/json; charset=utf-8'})
	s1.post(uri ,json_payload)
			

	
			


login()
loopy()