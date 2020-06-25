# -*- coding: utf-8 -*-
import requests, json,pytest,yaml,ddt,os
from commen.common import wm_url,wm_headers


'''

url = 域名    (  wm_url()  )
data = body
headers = headers (   wm_heraders   )
pytest --html=./report/微盟智慧酒店-接口自动化测试报告.html  指定报告路径

'''


@ddt.ddt
class Test_order:

    #业务-房态维护查询
    @ddt.file_data(os.path.dirname(os.path.dirname(__file__)) + "/source/" + 'test_getListStatus.yaml')
    def test_getListStatus(self,**kwargs):

        url = wm_url() + "/pcaal/core/roomPricePlan/getListStatus"
        data = kwargs.get('testdata')
        json_data = json.dumps(data)
        headers = wm_headers()

        s = requests.post(url=url,data=json_data,headers=headers)

        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a
        print("业务-房态维护查询")

    #业务-房价管理-全部房型
    @ddt.file_data(os.path.dirname(os.path.dirname(__file__)) + "/source/" + 'test_getRoomTypeList.yaml')
    def test_getRoomTypeList(self,**kwargs):
        url = wm_url() + "/pcaal/core/roomPricePlan/getRoomTypeList"
        data = kwargs.get('testdata')
        json_data = json.dumps(data)
        headers = wm_headers()

        s = requests.post(url=url,data=json_data,headers=headers)

        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a
        print("业务房价管理-全部房型")

    #业务-房价管理-房价计划查询
    @ddt.file_data(os.path.dirname(os.path.dirname(__file__)) + "/source/" + 'test_getListType.yaml')
    def test_getListType(self,**kwargs):
        url = wm_url() + "/pcaal/core/roomPricePlan/getListType"
        data = kwargs.get('testdata')
        json_data = json.dumps(data)
        headers = wm_headers()

        s = requests.post(url=url,data=json_data,headers=headers)

        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a
        print("业务房价管理-房价计划查询")