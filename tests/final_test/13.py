from ipaddress import *

net = ip_network("91.147.200.0/255.255.252.0", strict=False)
cnt = 0
for ip in net.hosts():
    if bin(int(ip))[2:].count("1") % 5 == 2:
        cnt += 1
print(cnt)
