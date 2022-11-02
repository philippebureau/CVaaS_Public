#!/usr/bin/python
###### README ######
# This can be used to test API and service token access to CVP on-prem
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
#INSERT YOUR SERVICE ACCOUNT TOKEN BELOW
token = '<token>'
#SET YOUR CVP HOSTNAME OR IP
CVP = 'CVP'
####

clnt = CvpClient()
#clnt.connect(nodes=[CVP], username='', password='', is_cvaas=True, cvaas_token=token)
clnt.connect(nodes=[CVP], username='', password='', api_token=token)
result = clnt.api.get_cvp_info()
print (result)
