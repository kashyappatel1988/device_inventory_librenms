#!/usr/bin/python
# script function - this script will do a curl API to the librenms and sort the output basis on the IP address 
#  for each librenms host x-auth token needs to be created on the librenms manually 
import sys
import subprocess
import socket
import argparse
from multiprocessing import Pool
import json 
import csv 
# from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from getpass import getpass
from pprint import * 

d = {}
ansible_hosts={}

d = {
     "sv3":"9fbce85788d56970104d0e7af2662323",
     "dl1":"03f0296286df9fcb16c4b481ab84dff5",
     "dc10":"081fc600fde6962c77eaa3e9f56bbc12",
     "sn1":"ae26857d4dd9f5ae87196f0a8787adcc",
     "ty6":"595f0520a7a14a1b0b3b8a2344631c49",
     "am1":"63ddffbef0ad2e18ee525419d17b6064",
     "am6":"e37186133d3d189792439bcf00528a46",
     "pdx1":"defcf7f9c0a246769a92bf27fc889a03",
    }


# # encrypted secrets with console password
# d2 = {'dc10': 'c2MAAtFwt2lWvNjq3N/3vfij2DKF0y2Q6AWgbRRtwMlpKtVr9bolMShgvAzJp9ta0ugz/73qFYavxPUfg+XdIbmAaio14cOcsDVdCAOBq2vXAOzR3I1G0CXaas9jlY1xIpbtjA==', 
# 'sn1':'c2MAAhOLvOoUDPGI7Y7niVgQsy3OgX7J7/pFkSuDo1lfU9Jte+HXhsk8/E3f9eCZNw74w7uj6jJewFiplqCgWdRtOsPGTPlwAG2mgfDfh7BuGsj6oQ0H7TNkC51YW8V3alrsDQ==',
# 'dl1': 'c2MAAtKY6RrI0250QKvNitTF9UZwkfaRsmtgn4ktiu8AUotabnuFscpCQv+YZSBt7utM120dPzk3jPQt6cH3JtcgBf/Q7xyMd5VA+TBfFMuIDKmkDTezczBnWR1GvVwfVJwikw==', 
# 'am1': 'c2MAAlxsGiVt3+N6qiyEJ6NEY1b9VONcIzCDPVdocyj1nftu/XO3SNQ65SnAdNPJJDM3UfRx4XuCth+TEqiQHNUsTmp44+iSAFaRVKZnDAlHyD/xdXqLOnCrzwz9S9M5MUqotg==', 
# 'pdx1': 'c2MAAqnNn4xs9uu3/qcTpzHsxUnljDRtyYzNF7d96fntnCSEFm/HH2WQnBA68WWHsusgx1DijIMvUjw8oaldwIs/px9hbU+wA80WFwTiZ4LGKCcqn3GGdl4bcleukFJgxdldaw==', 
# 'ty6': 'c2MAAv/hNSlqjUs11vO8/GDuPhhXx8zA5MP7usRyqdM5vyPsKFa/LVDFk4oLhWLVexycaxATnNKcwsurIoBO2BQ94pRTsukFxMjxlYPPY8hoWb8+iAmN9lnY8I6BB1xdOPMwqw==', 
# 'sv3': 'c2MAAp8nWTkP6t2EO6NKKkUp6uEeBetkEo9iYxgPWb4e3Jr4ykhMWr/shg9uBpJFZmc1E+0WpGLXRNWyIJTenYOgrUEw66oCVOQ7DANxr0Yl4p936T7E45sMoqwhfodOGOoQGw==', 
# 'am6': 'c2MAAtY8L5mqIKlK4k071B7FJlcrvxLaWXIkzgCZFsbJLa/YzfU8U5+MS21RgQVYI8jXEr3lPVUNqeY0mppemQplIuP5Hv4xltfK5H/XGj7P+Kxkpf9qU6w4VUra20pVGkwL7A=='}

# passwd = getpass()
# for k,v in list(d2.items()):
#     d[k] =decrypt(passwd,b64decode(v))


def lmns_api():
    ls = []
    result = {}
    for dc in list(d.keys()):
        if dc != 'pdx1':
            curl1 = ''' curl -H 'X-Auth-Token: %s' https://%s-librenms01.pan.local/api/v0/devices?all -ks ''' %(d[dc],dc)
            op1 = json.loads(subprocess.check_output(curl1,shell=True))
            ls.append(op1)
        else:
            curl1 = ''' curl -H 'X-Auth-Token: %s' https://%s-librenms.pan.local/api/v0/devices?all -ks ''' %(d[dc],dc)
            op1 = json.loads(subprocess.check_output(curl1,shell=True))
            ls.append(op1)
    # print ls 
    return ls
'''
This function will access the values of dictonary which has been retrived by lmns_api function 
dictionary structure 
Result = [ 
am1:{
devices:[{ip : 10.107.255.32 , hostname:am1010301-ipmi.pan.local,OS:arista_eos,Platform:4.14.2F,Hardware:DCS-7010T-48}, {device2 info},{device3 info}......,{device N info}]    
}, 
sv3:{ 
devices:[{ip : 10.107.255.32 , hostname:am1010301-ipmi.pan.local,OS:arista_eos,Platform:4.14.2F,Hardware:DCS-7010T-48}, {device2 info},{device3 info}......,{device N info}]
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
            ansible_hosts[dc['devices'] [device] ['hostname']] = [dc['devices'] [device] ['ip'],dc['devices'] [device] ['version'],dc['devices'] [device] ['hostname'],dc['devices'] [device] ['hardware']]
            # d[dc['devices']['hostname']] = [dc['devices'] [device] ['ip'],dc['devices'] [device] ['os'],dc['devices'] [device] ['version'],dc['devices'] [device] ['hardware']]
            count+=1
    return d,ansible_hosts

# # Function to Sort Parsed OUTPUT of CURL API to the Libernms

# def dlist_csv(result=[],*args):
#     print result[0]
#     for m in result:
#         for l in range(result[m]['devices']):
#             print result[m]['devices'][l]['ip'], result[m]['devices'][l]['hostname'],result[m]['devices'][l]['version'],result[m]['hardware'][l]['ip']


dl = lmns_api()
# print dl
dlist_print(dl)
# dlist_csv(dl)
