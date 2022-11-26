import requests
import json
with open("serverList.txt","r") as serverList:
  for server in serverList.readlines():
    response = requests.get("https://" + server.rstrip() + "/redfish/v1/Systems/System.Embedded.1",verify=False,auth=('root','calvin'))
data = response.json()
print (data[u'PowerState'])
