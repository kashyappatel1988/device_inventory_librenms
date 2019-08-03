#!/usr/bin/python
# script function - this script will do a curl API to the librenms and sort the output basis on the IP address 
#  for each librenms host x-auth token needs to be created on the librenms manually 
import sys
import argparse
import json 
# from simplecrypt import encrypt, decrypt

d = {
     "dc1":"####",
     "dc2":"####",
     "dc3":"####",
     "dc4":"####",
     "dc5":"####",
     "dc6":"####",
     "dc7":"####",
     "dc8":"####"
    }

def lmns_api():
    ls = []
    result = {}
    for dc in list(d.keys()):
        if dc != 'pdx1':
            curl1 = ''' curl -H 'X-Auth-Token: %s' https://%s-librenms01.xyzlocal/api/v0/devices?all -ks ''' %(d[dc],dc)
            op1 = json.loads(subprocess.check_output(curl1,shell=True))
            ls.append(op1)
        else:
            curl1 = ''' curl -H 'X-Auth-Token: %s' https://%s-librenms.xyzlocal/api/v0/devices?all -ks ''' %(d[dc],dc)
            op1 = json.loads(subprocess.check_output(curl1,shell=True))
            ls.append(op1)
    # print ls 
    return ls
'''
This function will access the values of dictonary which has been retrived by lmns_api function 
dictionary structure 
Result = [ 
am1:{
devices:[{ip : 100.107.255.32 , hostname:am1010301-ipmi.xyzlocal,OS:arista_eos,Platform:4.14.2F,Hardware:DCS-7010T-48}, {device2 info},{device3 info}......,{device N info}]    
}, 
sv3:{ 
devices:[{ip : 100.107.255.32 , hostname:kpkpk-ipmi.kpkp.local,OS:arista_eos,Platform:4.14.2F,Hardware:DCS-7010T-48}, {device2 info},{device3 info}......,{device N info}]
}
]
'''

def dlist_print(result=' ',*args):
    d = {}
    count = 0
    print("==============================================================================================================================================================")
    print(("{0:4}    {1:40}   {2:25}     {3:25} {4:25}    {5:25}".format('Count','IP' ,'HOSTNAME', 'OS','Platform','Hardware')))
    print("==============================================================================================================================================================")
    for dc in result:
        for device in range(0,len(dc['devices'])):
            # print dc['devices'][0]['hostname']
            print(("{!s:5}    {!s:40}   {!s:25}     {!s:25} {!s:25}   {!s:25} ".format(str(count),dc['devices'] [device] ['hostname'], dc['devices'] [device] ['ip'] ,dc['devices'] [device] ['os'],dc['devices'] [device] ['version'],dc['devices'] [device] ['hardware'])))
            count+=1
    return d


dl = lmns_api()
dlist_print(dl)
