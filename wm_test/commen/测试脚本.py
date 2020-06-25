# coding:utf-8

import requests
import json

def getToken():
        getCodeRsUrl = 'http://account.saas.weimobqa.com/website/saas/account/api2/user/getCodeRs'
        loginUrl = 'http://account.saas.weimobqa.com/website/saas/account/api2/user/login'


        r = requests.session()
        jsondata = {"zone": "0086", "phoneNumber": "17621646720", "pagename": "login"}
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        #getcoders
        r.post(url=getCodeRsUrl, json=jsondata, headers=headers)

        # login
        # headers = {'Content-Type': 'application/json;charset=UTF-8'}
        loginJson = {"zone": "0086", "phone": "17621646720", "password": 'admin123456'}
        print(loginJson)
        response = r.post(url=loginUrl, json=loginJson, headers=headers)
        # print("======================停止接口，response===================")
        data_res = response.json()
        print(data_res)
        if data_res["errcode"] == 0:
                print(response.text)
                print("签名生成成功")
                print(json.loads(response.text)['data']['token'])
                return json.loads(response.text)['data']['token']
        else:
                print("签名生成失败")

getToken()