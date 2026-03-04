from ipaddress import *

net = ip_network("93.65.153.170/255.255.255.192", 0)

for ip in net:
    print(ip)

# 93.65.153.190
print(93 + 65 + 153 + 190)