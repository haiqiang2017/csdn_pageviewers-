#/usr/bin/env python
# _*_ coding: utf-8 _*_
#
#update_author:jianghaiqiang
#
import sys
import requests
import random
import json
from utils import *
from apis import *
import time

cookie_list=["uuid_tt_dd=10_20719313010-1554114563508-311156; dc_session_id=10_1554114563508.377228; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=5744*1*Haiqiang1995!6525*1*10_20719313010-1554114563508-311156; SESSION=7d667dc5-fb2c-4fe3-b2c3-43bcbbd83482; UserName=Haiqiang1995; UserInfo=6782551b82dc482a9efcfe9b8cb74bda; UserToken=6782551b82dc482a9efcfe9b8cb74bda; UserNick=%E8%B5%B7%E7%82%B9%E7%9A%84%E4%B8%93%E5%88%8A; AU=413; UN=Haiqiang1995; BT=1554366654505; hasSub=true; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1554114564,1554366759,1554367005,1554619137; dc_tos=ppl6cj; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1554632803"
]
class get_cookie(object):

    def __init__(self):
        pass
    def get_random_cookie(self):
        return random.choice(cookie_list)

if __name__ == '__main__':
    pass
