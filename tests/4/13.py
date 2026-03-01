from ipaddress import *
mn = 10 ** 7

for mask in range(10, 32):
    net1 = ip_network(f"24.110.109.185/{mask}", 0)
    net2 = ip_network(f"24.110.109.179/{mask}", 0)
    if net1 == net2:
        cnt = 0
        for ip in net2:
            cnt += 1
    mn = min(mn, cnt)
print(mn)