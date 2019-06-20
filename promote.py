
import json
import requests
import time

def main():
	requests.packages.urllib3.disable_warnings()
	base_url = "https://192.168.100.12:9440/api/nutanix/v0.8/"
	s = requests.Session()
	s.auth=('admin','F1berP@chs')
	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})

	data = s.get(base_url + 'protection_domains', verify=False).json()
	for e in data['entities']:
		active = e['active']
		if Name.find('CriticalAppsNoho') == 0:
			print (active)


 

if __name__ == "__main__":
  main()
