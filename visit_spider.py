#coding:utf-8
import random
import urllib3
import time
from cookie_pool import get_cookie
from UserAgent_pool import get_UserAgent
import requests

"""提取数据访问链接"""
# 禁用urllib3的警告
urllib3.disable_warnings()

class visitSpider(object):
    def __init__(self):
        self.ua = get_UserAgent().get_random_useragent()
        self.cookie = get_cookie().get_random_cookie()
        # print self.ua,self.cookie
        # 处理 headers
        self.headers = {"User-Agent": self.ua, "cookie": self.cookie}

        self.urls = []
        self.nums = 0
        self.currentHour = time.localtime().tm_hour

    def readFile(self):
        """"""
        self.nums += 0
        with open("download/url.txt", "r") as f:
            for i in f.readlines():
                url = i[:-2]
                if self.checkClone(url,self.urls):
            #        print("\r读取url:",i)
                    self.urls.append(i[:-2])
                    self.nums += 1

    def checkClone(self,urls,list):
        """判重"""
        flag = 0
        if len(list) > 0:
            for i in list:
                if list == urls:
                    flag = 1
        if flag == 1:
            return 0
        return 1

    def visit(self):
        request = urllib3.PoolManager()
        # 计算时间
        timeNum = 0
        # 计算次数
        listNum = 0
        while True:
            # 访问时间 8 12 18 20
            #if self.currentHour == 0 or self.currentHour == 1 or self.currentHour == 20 or self.currentHour == 1:
            if self.currentHour:
                # 得到url值
                url = self.urls[random.randint(0,self.nums - 1)]
                # 使用urllib3发送请求
               # response = request.request('GET', url, headers=self.headers)
                response = requests.get(url,headers= self.headers)
              #  print response.content
               # break
                # 打印返回信息
                print(url,response.status_code,listNum,str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min))
                # 访问一次睡一秒
                time.sleep(random.choice(range(1,3)))
                timeNum += 1
                listNum += 1
                # 每访问50次睡30秒
                if listNum % 50 == 0:
                    for i in range(random.choice(range(25,30))):
                        print("\r剩余休息时间：%d秒"%(30-i))
                        time.sleep(1)
                # 当到达一定时间（1个小时）之后重新读取文档
                if timeNum%3600==0:
                    self.readFile()
            else:
                print("休息中,当前时间：" + str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min)
                      + ":" + str(time.localtime().tm_sec) + " ...")
                time.sleep(1)

def Main():
    vi = visitSpider()
    vi.readFile()
    vi.visit()

if __name__ == "__main__":
    Main()
