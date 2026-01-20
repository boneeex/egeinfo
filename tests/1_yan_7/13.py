from ipaddress import *

net = ip_network("172.16.160.0/255.255.240.0")
cnt = 0
for ip in net:
    if ip not in [net[0], net[-1]]:
        if bin(int(ip))[2:].count("1") % 4:
            cnt += 1

print(cnt)