#!/usr/bin/python
###### README ######
# THIS SCRIPT REQUIRED CVPRAC MODULE
# DOWNLOAD LOCATION: https://github.com/aristanetworks/cvprac

from cvprac.cvp_client import CvpClient
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests.packages.urllib3

#disable SSL warnings
requests.packages.urllib3.disable_warnings()

####
#USER INPUT
#INSERT YOUR TOKEN BELOW
token = '<CVaaS token>'
####

clnt = CvpClient()
clnt.connect(nodes=['www.arista.io'], username='', password='', is_cvaas=True, cvaas_token=token)

try:
  httpCode = urllib.request.urlopen("https://www.arista.io", timeout=5).getcode()
except:
  result = "CVaaS is unreachable, verify the network"
else:
  try:
    clnt.api.get_inventory()
  except:
    result = "Unauthorized Access, verify your token"
  else:
    result = "CVaaS connection successful"
print (result)
