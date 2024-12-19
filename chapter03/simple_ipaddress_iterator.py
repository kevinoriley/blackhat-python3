import ipaddress
#OR: from ipaddress import ip_address, ip_network

for ip in Ipv4Network("192.168.100.1/24"):
  s = socket.socket()
  s.connect((ip, 25))
  # send smtp packets
