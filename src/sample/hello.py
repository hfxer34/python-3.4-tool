#
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://yahoo.com/')
r.text
print(requests.get('http://ci.nii.ac.jp/ncid/BB08796640.json').json())

print('Hello World!!')

