from ipaddress import *

res = []
ip_net = IPv4Network("124.123.123.122/18", 0)
for part1 in range(255):
    for part2 in range(255):
        for part3 in range(255):
            for part4 in range(255):
                ip_net = IPv4Network(f"{part1}.{part2}.{part3}.{part4}/18", 0)
                c = str(int(ip_net.hostmask)).count("1")
                if c > 0 and c % 6 == 0:
                    res.append(ip_net.broadcast_address)

print(min(res))