#!/usr/bin/env python3
import json
import requests
import paramiko

import time

def main():
	requests.packages.urllib3.disable_warnings()
	base_url = "https://192.168.1.123:9440/api/nutanix/v0.8/"
	base_url_prism = "https://192.168.1.200:9440/PrismGateway/services/rest/v1/"
	s = requests.Session()
	s.auth=("admin","sdxsolutions")
	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})

	data = s.get(base_url + 'vms', verify=False).json()
	for e in data['entities']:
		vmUuid = e['uuid']
		vmConfig = e['config']
		vmName=vmConfig['name']
		if vmName.find('Server') == 0:
			#print (e)
			#print ('Power On VM ' + vmName + ' ' + vmUuid) 
			details = s.get(base_url_prism + 'vms/' + vmUuid,verify=False)
			rdetails= details.json()
			#print (rdetails)
			#print ("-------")
			IP = rdetails['ipAddresses']
			print (vmName + " IP " + IP[0])
			ssh = paramiko.SSHClient()
			ssh.load_system_host_keys()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(IP[0], username="root", password="password")
			ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("nohup ./stress/stress-ng-0.03.11/stress-ng --cpu 2 --timeout 10s >> /dev/null &")
			ret = ssh_stdout.read()
			err = ssh_stderr.read()
			

if __name__ == "__main__":
  main()
