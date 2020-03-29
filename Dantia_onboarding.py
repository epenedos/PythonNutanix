#!/usr/bin/env python3
import json
import requests
import time
import sys
import urllib3
from base64 import b64encode
import tkinter as tk


def build_cat(s,base_url,catname):
  body_cat = {
  "api_version": "3.1.0",
  "value": catname,
  "description": "Automated created for Tenant"}
  print(body_cat)
  r = s.request("PUT",base_url + 'categories/AppType/' + catname, data=json.dumps(body_cat),verify=False)
  return r
def build_appPolicy(s,base_url,catname,inbound):
    body_cat = {
    "api_version": "3.1.0",
    "value": catname,
    "description": "Automated created for Tenant"}

    r = s.request("PUT",base_url + 'categories/AppType/' + catname, data=json.dumps(body_cat),verify=False)
    return r

def main(argv):
  requests.packages.urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#  print 'Number of arguments:', len(sys.argv), 'arguments.'
#  print 'Argument List:', str(sys.argv)
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#  base_url = "https://192.168.86.20:9440/api/nutanix/v3/"
  base_url = "https://10.59.98.253:9440/api/nutanix/v3/"

  s = requests.Session()
  s.auth=("epenedos","Nutanix/4u$")
  s.headers.update({'Content-Type': 'application/json'})

  window = tk.Tk()
  window.title("Dantia OnBoarding")
  window.resizable(width=False, height=False)
  frm_entry = tk.Frame(master=window)
  ent_temperature = tk.Entry(master=frm_entry, width=10)
  lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
  ent_temperature.grid(row=0, column=0, sticky="e")
  lbl_temp.grid(row=0, column=1, sticky="w")
  btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=build_cat(s,base_url,argv[2])
    )
  frm_entry.grid(row=0, column=0, padx=10)
  btn_convert.grid(row=0, column=1, pady=10)

  window.mainloop()





  build_cat(s,base_url,argv[2])
  build_appPolicy(s,base_url,argv[2],argv[3])




if __name__ == "__main__":
  main(sys.argv[1:])
