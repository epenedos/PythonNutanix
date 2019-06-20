#!/usr/bin/env python3
import json
import requests
import time

def main():
	requests.packages.urllib3.disable_warnings()
	base_url = "https://85.190.178.17:9440/console/api/"
	s = requests.Session()
	s.auth=("admin","sdxsolutions")
	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})

	data = s.get(base_url + 'protection_domains/unprotected_vms/').json()
	print (data)


if __name__ == "__main__":
  main()
