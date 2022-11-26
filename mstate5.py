import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ips = ['10.114.142.88', '10.114.142.93', '10.114.142.89', '10.114.142.86', '10.114.142.91', '10.114.142.94', '10.114.142.90', '10.114.142.87', '10.114.142.92']
for ip in ips:
    response = requests.get("https://" + ip +
"/redfish/v1/Systems/System.Embedded.1",verify=False,auth=('root','calvin'))
    data = response.json()
    print(ip + " is Powered " + data[u'PowerState'])
