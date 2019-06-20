#!/usr/bin/env python3
import json
import requests
import time
import http.client
import winrm



requests.packages.urllib3.disable_warnings()




def login():
	global base_url 
	base_url= 'https://10.21.47.37:9440/api/nutanix/v2.0/'
	global s
	s = requests.Session()
	s.auth=('admin','nx2Tech701!')
	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
	global vmUuid
	
#	s = winrm.Session('10.21.5.253', auth=('Administrator', 'nutanix/4u!'))
#	r = s.run_cmd('ipconfig', ['/all'])
#	print(r.status_code)

#	print(r.std_out)
	
	
	

def listVG():
	data = s.get(base_url + 'volume_groups', verify=False).json()
	return data
	
def listVM():
	data = s.get(base_url + 'vms', verify=False).json()
	return data
	
def listVMbyUuid(Uuid):
	data = s.get(base_url + 'vms/'+Uuid, verify=False).json()
	return data
		
def getTask(Uuid):
	data = s.get(base_url + 'tasks/'+Uuid, verify=False).json()
	return data
	
def cloneVGandAttach():	
	vgdata = listVG()
	i = 0
	print("")
	for e in vgdata['entities']:
		vGUuid = e['uuid']
		vGName=e['name']
		print (str(i) + " - " + vGName)
		i=i+1
	print("")
	opt = input("choose an Volume Group ")
	if opt is "":
		return
	vGName=vgdata['entities'][int(opt)]['name']
	vGUuid=vgdata['entities'][int(opt)]['uuid']
	power = s.post(base_url + 'volume_groups/' + vGUuid + '/clone/',json.dumps({"name": "Clone - "+vGName})).json()
	newVG=getTask(power['task_uuid'])
	
	newVGUuid = newVG['entity_list'][1]
#	print (newVGUuid['entity_id'])
	vmdata= listVM()
	i=0
	print("")
	for e in vmdata['entities']:
		vMUuid = e['uuid']
		vMName=e['name']
		print (str(i) + " - " + vMName)
		i=i+1
	print("")
	opt = input("choose an VM to attach Volume Group ")
	if opt is "":
		return
	vMName=vmdata['entities'][int(opt)]['name']
	vMUuid=vmdata['entities'][int(opt)]['uuid']

	power = s.post(base_url + 'volume_groups/' + newVGUuid['entity_id'] + '/attach/',json.dumps({"operation": "ATTACH","vm_uuid":vMUuid}))
	
	

def listVGandAttach():	
	vgdata = listVG()
	i = 0
	print("")
	for e in vgdata['entities']:
		vGUuid = e['uuid']
		vGName=e['name']
		print (str(i) + " - " + vGName)
		i=i+1
	print("")
	opt = input("choose an Volume Group ")
	if opt is "":
		return
	vGName=vgdata['entities'][int(opt)]['name']
	vGUuid=vgdata['entities'][int(opt)]['uuid']
	print("")
	vmdata= listVM()
	i=0
	for e in vmdata['entities']:
		vMUuid = e['uuid']
		vMName=e['name']
		print (str(i) + " - " + vMName)
		i=i+1
	print("")
	opt = input("choose an VM to attach Volume Group ")
	if opt is "":
		return
	vMName=vmdata['entities'][int(opt)]['name']
	vMUuid=vmdata['entities'][int(opt)]['uuid']

	power = s.post(base_url + 'volume_groups/' + vGUuid + '/attach/',json.dumps({"operation": "ATTACH","vm_uuid":vMUuid}))
	
def detachVG():	
	vgdata = listVG()
	i = 0
	print("")
	for e in vgdata['entities']:
		if 'attachment_list' in e:
			vGUuid = e['uuid']
			vGName=e['name']
			vGAttachVM=e['attachment_list']
			print (str(i) + " - " + vGName)
			for j in vGAttachVM:
				vmUuid=j['vm_uuid']
				datavm=listVMbyUuid(vmUuid)
				print ("		VM " + datavm['name'])
		i=i+1
	print("")
	opt = input("choose an Volume Group ")
	if opt is "":
		return
	
	vGName=vgdata['entities'][int(opt)]['name']
	vGUuid=vgdata['entities'][int(opt)]['uuid']
	vGAttachVM=vgdata['entities'][int(opt)]['attachment_list']
	
	i=0
	for j in vGAttachVM:
		vmUuid=j['vm_uuid']
		datavm=listVMbyUuid(vmUuid)
		print("")
		print (str(i) + " - " + datavm['name'])
		i=i+1
	opt = input("choose an VM to detach Volume Group ")
	if opt is "":
		return
	vMUuid=vGAttachVM[int(opt)]['vm_uuid']
	print(vMUuid)
	power = s.post(base_url + 'volume_groups/' + vGUuid + '/detach/',json.dumps({"operation": "ATTACH","vm_uuid":vMUuid}))
	
def deleteVG():	
	vgdata = listVG()
	i = 0
	print("")
	for e in vgdata['entities']:
		if 'attachment_list' not in e:
			vGUuid = e['uuid']
			vGName=e['name']
			print (str(i) + " - " + vGName)
		i=i+1
	print("")
	opt = input("choose an Volume Group ")
	if opt is "":
		return
	vGUuid=vgdata['entities'][int(opt)]['uuid']

	power = s.delete(base_url + 'volume_groups/' + vGUuid )
	
			

def loopy():	
	while 1:
		print("")
		print("")
		print("1-listVG and Attach to VM")
		print("2-CloneVG and attach to VM")
		print("3-Detach VG from VM")
		print("4-Delete VG")
		print("")
		print("99 - Exit")
	
		opt = input("choose an option ")
		
		if opt == "1":
			listVGandAttach()
			
		if opt == "2":
			cloneVGandAttach()
		if opt == "3":
			detachVG()
		if opt == "4":
			deleteVG()
					
		
		if opt == "99":
			break;



			


login()
loopy()