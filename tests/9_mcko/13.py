from ipaddress import *

net = list(ip_network("115.140.105.247/255.192.0.0", 0).hosts())
print(net[-2])
print(115 + 191 + 255 + 253)