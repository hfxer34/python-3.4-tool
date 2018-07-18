import json
import sys
import requests

def main(zipcode):
    url = "http://zipcloud.ibsnet.co.jp/api/search"
    param = {"zipcode": zipcode}

    res = requests.get(url, params=param)

    print('http response code =', res.status_code)
    print('http response headers =', res.headers)
    print('http response text =', res.text)

    response = json.loads(res.text)
    address = response["results"][0]
    print(address["address1"] + address["address2"] + address["address3"])
    print(address["kana1"] + address["kana2"] + address["kana3"])

    print("〒" + address["zipcode"] + "は" + address["address1"] + address["address2"] + "の郵便番号です。")

main(sys.argv[1])
