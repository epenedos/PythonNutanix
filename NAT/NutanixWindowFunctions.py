#!/usr/bin/env python3
import json
import requests
import time
import sys
import urllib3
import tkinter as tk
from tkinter import *
from base64 import b64encode
import NutanixAutoFunctions
import NutanixAuto


class winClusterConnect(Toplevel):
    def __init__(self, parent, title = None):

        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.parent = parent

        if len(title) > 0: self.top.title(title)

        Label(self.top, text="Cluster PC IP:").grid(row=0)
        Label(self.top, text="User ID:").grid(row=1)
        Label(self.top, text="Password:").grid(row=2)
        self.cip = StringVar()
        self.userid = StringVar()
        self.password = StringVar()

        self.cip = tk.Entry(self.top)
        self.userid = tk.Entry(self.top)
        self.password = tk.Entry(self.top)
        self.cip.grid(row=0, column=1)
        self.userid.grid(row=1, column=1)
        self.password.grid(row=2, column=1)
        self.top.bind("<Return>", self.ok)
        self.top.bind("<Escape>", self.cancel)
        self.top.focus_set()

        Button(self.top, text="OK", command=self.ok).grid(row=5,column=1,pady=5)

        self.top.mainloop()

    def ok(self, event=None):
        self.cip = self.cip.get()
        self.userid = self.userid.get()
        self.password = self.password.get()

        NutanixAuto.ntxinstance.clusterConnect(self.cip,self.userid,self.password)
        self.top.destroy()

    def cancel(self, event=None):
        self.top.destroy()
