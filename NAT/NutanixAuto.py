#!/usr/bin/env python3
import json
import requests
import time
import sys
import urllib3
from base64 import b64encode
from tkinter import Tk, Frame, Menu
import tkinter
from NutanixAutoMenu import MenuBar
from NutanixWindowFunctions import winClusterConnect
from NutanixAutoFunctions import ClusterConnect

class Application:
    def __init__(self):
        # Create and display a test window for viewing the menus
        window = tkinter.Tk()
        window.minsize(500, 500)
        window.title("Nutanix Automation Tool")
        window.wm_title = "NAT"


        # Create an instance of the MenuBar class and display it to the window
        mb = MenuBar(window)
        # window.config(menu = mb)

        window.mainloop()

if __name__ == '__main__':
    Application()
