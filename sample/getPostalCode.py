#
import requests

print(requests.get('http://zipcloud.ibsnet.co.jp/api/search?zipcode=1540013').json())

print('============= End')
