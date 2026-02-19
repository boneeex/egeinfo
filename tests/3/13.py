import ipaddress

net = ipaddress.IPv4Network("17.234.25.1/255.255.224.0", strict=False)

print(net.broadcast_address) 
print(17 + 234 + 31 + 255)