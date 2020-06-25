# -*- coding: utf-8 -*-
import sys
import os
# from wm_test.commen.login import getToken
# import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
def wm_url():
    url = "http://master.saas.weimobqa.com/api3/hotel"
    return url

def wm_headers():
    # headers = {"Content-Type": "application/json",
    #            "Authorization": "Bearer " + getToken()}

    headers = {"Content-Type": "application/json",
               "Authorization": "Bearer 38824e827d141ad01ae7054290bc9c2d4ee8ca274adffb7e61603e52cc09214f"}
    return headers

