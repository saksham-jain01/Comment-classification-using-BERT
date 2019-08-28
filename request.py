#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:29:55 2019

@author: msf
"""
import requests

# URL
url = "http://localhost:5000/result"

# Change the value of experience that you want to test
r = requests.post(url,json={"text":"ok, helpful",})
print(r.json())