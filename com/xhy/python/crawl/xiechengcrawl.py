# -*- coding: utf-8 -*-
import requests
import json
import random




class xiechengcrawl(object):
    def __init__(self, headers, request_payload):
        self.url ="https://flights.ctrip.com/international/search/api/search/batchSearch?v={}".format(random.random)
        self.headers = headers
        self.request_payload = request_payload


    def run(self):
        print("进入方法")
        response = requests.post(self.url, data=json.dumps(self.request_payload), headers=self.headers)
        list = json.loads(response.content.decode())
        cookies = response.cookies.get_dict()
        return list['data']['context']['searchId']

def buildheaders1():
    headers1 = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://flights.ctrip.com",
        "referer": "https://flights.ctrip.com/international/search/oneway-hkg-bkk?depdate=2019-11-13&cabin=y_s&adult=1&child=0&infant=0",
        "sign": "0045ba0ca7ea4a038db3d82a1fe096d4",
        "transactionid": "9f8d4a310d894a4ab23345ca063b930c",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    return headers1


def buildrequestpayload1():
    request_payload1 = {"flightWayEnum":"OW","arrivalProvinceId":0,"extGlobalSwitches":{"useAllRecommendSwitch":"true"},"arrivalCountryName":"泰国","infantCount":0,"cabin":"Y_S","cabinEnum":"Y_S","departCountryName":"中国","flightSegments":[{"departureDate":"2019-11-09","arrivalProvinceId":0,"arrivalCountryName":"泰国","departureCityName":"香港","departureCityCode":"HKG","departureCountryName":"中国","arrivalCityName":"曼谷","arrivalCityCode":"BKK","departureCityTimeZone":random.randint(460,500),"arrivalCountryId":random.randint(1,20),"timeZone":480,"departureCityId":58,"departureCountryId":1,"arrivalCityTimeZone":420,"departureProvinceId":32,"arrivalCityId":random.randint(300,400)}],"childCount":0,"segmentNo":1,"adultCount":1,"extensionAttributes":{"isFlightIntlNewUser":"false"},"transactionID":"9f8d4a310d894a4ab23345ca063b930c","directFlight":"false","departureCityId":58,"isMultiplePassengerType":0,"flightWay":"S","arrivalCityId":random.randint(300,400),"departProvinceId":32}
    return request_payload1


class xiecheng2(object):
    def __init__(self, searchId , headers, request_payload):
        self.url ="https://flights.ctrip.com/international/search/api/search/pull/{}?v={}".format(searchId,random.random())
        print(self.url)
        self.headers = headers
        self.request_payload = request_payload


    def run(self):
        print("进入方法")
        response = requests.post(self.url, data=json.dumps(self.request_payload), headers=self.headers)
        list = json.loads(response.content.decode())
        print(response.content.decode())

def buildheaders2():
    headers2 = {

        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://flights.ctrip.com",
        "referer": "https://flights.ctrip.com/international/search/oneway-hkg-bkk?depdate=2019-11-09&cabin=y_s&adult=1&child=0&infant=0",
        "sign": "0045ba0ca7ea4a038db3d82a1fe096d4",
        "transactionid": "9f8d4a310d894a4ab23345ca063b930c",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    return headers2


def buildrequestpayload2():
    request_payload1 = {"flightWayEnum":"OW","arrivalProvinceId":0,"extGlobalSwitches":{"useAllRecommendSwitch":"true"},"arrivalCountryName":"泰国","infantCount":0,"cabin":"Y_S","cabinEnum":"Y_S","departCountryName":"中国","flightSegments":[{"departureDate":"2019-11-09","arrivalProvinceId":0,"arrivalCountryName":"泰国","departureCityName":"香港","departureCityCode":"HKG","departureCountryName":"中国","arrivalCityName":"曼谷","arrivalCityCode":"BKK","departureCityTimeZone":480,"arrivalCountryId":4,"timeZone":480,"departureCityId":58,"departureCountryId":1,"arrivalCityTimeZone":420,"departureProvinceId":32,"arrivalCityId":359}],"childCount":0,"segmentNo":1,"adultCount":1,"extensionAttributes":{"isFlightIntlNewUser":"false"},"transactionID":"9f8d4a310d894a4ab23345ca063b930c","directFlight":"false","departureCityId":58,"isMultiplePassengerType":0,"flightWay":"S","arrivalCityId":359,"departProvinceId":32}
    return request_payload1


if  __name__ == '__main__':
    headers1 = buildheaders1()  #  构建请求头
    request_payload1 = buildrequestpayload1()  #  构建入参数
    x1 = xiecheng1(headers1,request_payload1)  #  实例化对象
    searchId = x1.run()  #  运行获取searchId进行拼接地址
    headers2 = buildheaders2()  # 构建请求头
    request_payload2 = buildrequestpayload2()  # 构建入参数
    x2 = xiecheng2(searchId, headers2, request_payload2)  # 实例化对象
    x2.run()  # 运行获取数据


