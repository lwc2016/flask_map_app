# encoding: utf-8
import requests
def googleToBaidu(lng, lat):
    url = "http://api.map.baidu.com/geoconv/v1/?coords={},{}&from=3&to=5&ak=IFGBl3dI3WlaABQh3cNm1UILTEUrTO0d".format(lng,lat)
    resp = requests.get(url).json()
    return resp
