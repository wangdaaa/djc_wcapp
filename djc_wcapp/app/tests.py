import os

from django.test import TestCase

# Create your tests here.
import requests

# from djc_wcapp.settings import AppID, AppSecret
#
# url="https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code=JSCODE&grant_type=authorization_code".format(AppID,AppSecret)
#
#
# res=requests.get(url=url)
# print(res)
# print(res.json())
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#
# print(a,'a=-====')
# #
# from djc_wcapp.settings import MEDIA_ROOT
# import time
#
# a = os.path.join(MEDIA_ROOT, str(time.time()))
# print(a)
# # with open(os.path.join(MEDIA_ROOT, str(time.time())), 'w+') as e:
from djc_wcapp.settings import MEDIA_ROOT

image='你好.png'
import hashlib
m=hashlib.md5()
import time
if image.split('.')[1] in ("png",):
    name=image.split('.')[0]
    m.update((str(time.time())+name).encode('utf8'))
    print(m.hexdigest(),'sssss')



data= {"username": "cloudAdmin ", "password": "N0!hI#3YXC!MA#$o"}
import json
url="http://10.130.9.36:30015/cloudbase/api/v1/auth/login"
# url="http://10.130.9.36:30015/cloudbase/api/v1/auth/login"
# u="http://10.130.9.36:30303/cloudbase/api/v1/auth/login"
headers_dict = requests.post(url=url, data=json.dumps(data), verify=False)
print(headers_dict)
print(headers_dict.json())

os.remove(os.path.join(MEDIA_ROOT,"20024.png"))