>This script will provide device list with IP,hostname,OS,platform. The data source is librenms so if there is any devices missing on the librenms it will not appear in this list



## Prerequisites
Secrets are encrypted with console passwords. If you do not know please contact Network engineering



### Usage 

```
git clone https://github.pan.local/networking/Network-devices-inventory
chmod +x *
./device_inventory.py 
```



## Python version consideration
This script works on python2.7 if you have python3+ then there may be some function may not work properly.
As a workaround you can install python 2.7 and change the scripts interpretor to !#/usr/bin/python2.7 ( or whatever python2.7 path you have in your system)

## Sample Output 

```
==============================================================================================================================================================
Count    IP                                         HOSTNAME                      OS                        Platform                     Hardware                 
==============================================================================================================================================================
    0    dc10-librenms01.pan.local                  10.106.122.180                linux                     3.10.0-862.2.3.el7.x86_64   Generic x86 64-bit        
    1    dc1030101-ipmi.pan.local                   10.106.252.181                ios                       15.0(2)SG5                  catalyst4948              
    2    dc1030101.pan.local                        10.106.252.176                arista_eos                4.14.9M                     DCS-7050TX-64             
    3    dc1030201-ipmi.pan.local                   10.106.252.182                ios                       12.2(25)EWA6                catalyst4948              
    4    dc1030201.pan.local                        10.106.252.177                arista_eos                4.14.9M                     DCS-7050TX-64             
    5    dc1030301-ipmi.pan.local                   10.106.252.183                ios                       12.2(25)EWA5                catalyst4948              
    6    dc1030301.pan.local                        10.106.252.178                arista_eos                4.14.9M                     DCS-7050TX-64             
    7    dc1030401-ipmi.pan.local                   10.106.252.184                ios                       12.2(54)SG                  catalyst4948              

```
