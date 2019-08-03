>This script will provide device list with IP,hostname,OS,platform. The data source is librenms so if there is any devices missing on the librenms it will not appear in this list, It is leveraging Librenms API and parse the output from json to text 


## Python version consideration
This script should work on both python2.7/3.7 plese report back any issues if it does not. 
## Sample Output 

```
==============================================================================================================================================================
Count    IP                                         HOSTNAME                      OS                        Platform                     Hardware                 
==============================================================================================================================================================
    0    dcx-librenms01.xyz.local                  100.100.122.180                linux                     3.10.0-862.2.3.el7.x86_64   Generic x86 64-bit        
    1    dcx30101-ipmi.xyz.local                   100.100.252.181                ios                       15.0(2)SG5                  catalyst4948              
    2    dcx30101.xyz.local                        100.100.252.176                arista_eos                4.14.9M                     DCS-7050TX-64             
    3    dcx30201-ipmi.xyz.local                   100.100.252.182                ios                       12.2(25)EWA6                catalyst4948              
    4    dcx30201.xyz.local                        100.100.252.177                arista_eos                4.14.9M                     DCS-7050TX-64             
    5    dcx30301-ipmi.xyz.local                   100.100.252.183                ios                       12.2(25)EWA5                catalyst4948              
    6    dcx30301.xyz.local                        100.100.252.178                arista_eos                4.14.9M                     DCS-7050TX-64             
    7    dcx30401-ipmi.xyz.local                   100.100.252.184                ios                       12.2(54)SG                  catalyst4948              

```
