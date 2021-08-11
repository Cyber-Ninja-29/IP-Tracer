import os
import urllib3_file
import json

while True:
    ip=input("What is Your IP:")
    url="http://ip-api.com/json/"
    response=urllibfile.urlopen(url + ip)
    data=response.read()
    values=json.loads(data)
    
    print("IP:" + values["query"])
    print("City:" + values["city"])
    print("ISP:" + values['isp'])
    print("country:" + values["country"])
    print("region:" + values["region"])
    print("Time:" + values["timezone"])


    break
    
