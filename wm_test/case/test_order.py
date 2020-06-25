# -*- coding: utf-8 -*-
import requests, json,pytest,yaml,ddt
from commen.test_r import read_yaml
from commen.common import wm_url,wm_headers


'''

url = 域名    (  wm_url()  )
data = body
headers = headers (   wm_heraders   )
pytest --html=./report/微盟智慧酒店-接口自动化测试报告.html  指定报告路径m


'''


@ddt.ddt
class Test_order:

    #住宿订单-订房订单
    @ddt.file_data(r'C:\Users\Public\Desktop\t1\wm_test\source\test_queryHotelBookOrderList.yaml')
    def test_queryHotelBookOrderList(self,**kwargs):

        url = wm_url() + "/pcaal/core/order/queryHotelBookOrderList"
        data = kwargs.get('testdata')  # 获取data
        json_data = json.dumps(data)  # 转json格式
        headers = wm_headers()

        s = requests.post(url=url,data=json_data,headers=headers)
        # token = json.dumps(s.text)
        # token_k = json.loads(token)
        # print(token_k)
        # with open('C:/Users/Public/Desktop/t1/wm_test/source/token.yaml',"w",encoding="utf-8") as f:
        #     yaml.dump(token_k,f,Dumper=yaml.RoundTripDumper,allow_unicode=True,width=1000)

        result = json.loads(s.text)                             #转为字典格式
        a = result["errmsg"]                                    #实际结果
        assert "处理成功" in a
        print("执行订房订单查询")

#住宿订单-住宿记录
    def test_queryHotelCheckInRecordList(self):
        url = wm_url() + "/pcaal/core/order/queryHotelCheckInRecordList"
        data = read_yaml("test_queryHotelCheckInRecordList.yaml")
        headers = wm_headers()
        s = requests.post(url=url,data=data,headers=headers)
        #print(s.text)
        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a

        print("执行住宿记录查询")

#商城订单—订单记录和预约订单为同一接口
    def test_queryGoodsOrderList(self):
        url = wm_url() + "/pcaal/core/order/queryGoodsOrderList"
        data = read_yaml("test_queryGoodsOrderList.yaml")
        headers = wm_headers()

        s = requests.post(url=url,data=data,headers=headers)
        #print(s.text)
        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a

        print("执行订单记录和预约订单查询")

#商城订单-核销记录
    def test_getVericationLogList(self):
        url = wm_url() + "/pcaal/core/usercode/getVericationLogList"
        data = read_yaml("test_getVericationLogList.yaml")
        headers = wm_headers()

        s = requests.post(url=url, data=data, headers=headers)
        #print(s.text)
        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a
        print("执行商城订单-核销记录查询")

#商城订单-预约记录
    def test_listBookRecord(self):
        url = wm_url() + "/pcaal/core/order/listBookRecord"
        data = read_yaml("test_listBookRecord.yaml")
        headers = wm_headers()

        s = requests.post(url=url, data=data, headers=headers)
        #print(s.text)
        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a
        print("执行商城订单-预约记录查询")

#堂食订单
    def test_listCanteenOrder(self):
        url = wm_url() + "/pcaal/core/canteen/order/listCanteenOrder"
        data = read_yaml("test_listCanteenOrder.yaml")
        headers = wm_headers()

        s = requests.post(url=url, data=data, headers=headers)
        #print(s.text)
        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a
        print("执行堂食订单查询")


#会员卡开卡订单
    def test_queryMemberCardOrderList(self):

        url = wm_url() + "/pcaal/core/order/queryMemberCardOrderList"
        data = read_yaml("test_queryMemberCardOrderList.yaml")
        headers = wm_headers()

        s = requests.post(url=url, data=data, headers=headers)
        #print(s.text)
        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a
        print("执行会员卡开卡订单查询")

#售后订单
    def test_getRefundOrderList(self):
        url = wm_url() + "/pcaal/core/order/getRefundOrderList"
        data = read_yaml("test_getRefundOrderList.yaml")
        headers = wm_headers()

        s = requests.post(url=url, data=data, headers=headers)
        #print(s.text)
        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a
        print("执行售后订单查询")

#售后设置查询
    def test_getAfterSaleSetting(self):
        url = wm_url() + "/pcaal/core/sharing/getAfterSaleSetting"
        data = read_yaml("test_getAfterSaleSetting.yaml")
        headers = wm_headers()

        s = requests.post(url=url, data=data, headers=headers)
       # print(s.text)
        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a
        print("执行售后设置查询")

#售后设置保存接口
    def test_addOrUpdateAfterSaleSetting(self):
        url = wm_url() + "/pcaal/core/sharing/addOrUpdateAfterSaleSetting"
        data = read_yaml("test_addOrUpdateAfterSaleSetting.yaml")
        headers = wm_headers()

        s = requests.post(url=url, data=data, headers=headers)  # 发送请求
       # print(s.text)
        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a
        print("执行售后设置保存")

#押金退款列表
    def test_getRefundPledgeOrderList(self):
        url = wm_url() + "/pcaal/core/order/getRefundPledgeOrderList"
        data = read_yaml("test_getRefundPledgeOrderList.yaml")
        headers = wm_headers()

        s = requests.post(url=url, data=data, headers=headers)
       # print(s.text)
        result = json.loads(s.text)
        a = result["errmsg"]
        assert "处理成功" in a
        print("执行押金退款列表")

#收款码订单
    def test_queryOrderListToB(self):
        url = wm_url() + "/pcaal/core/order/queryOrderListToB"
        data = read_yaml("test_queryOrderListToB.yaml")
        headers = wm_headers()

        s = requests.post(url=url, data=data, headers=headers)
        # print(s.text)
        result = json.loads(s.text)
        # print(result)
        a = result["errmsg"]
        assert "处理成功" in a
        print("执行收款码订单查询")