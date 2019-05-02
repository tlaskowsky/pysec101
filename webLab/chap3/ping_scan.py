#!/usr/bin/python
#-*- coding: utf-8 -*-

from scapy.all import IP
from scapy.all import ICMP
from scapy.all import sr1
import ipaddress

myip = '172.17.0.1'
netmask = '255.255.0.0'

def gen_iplist(ip, netmask):
    ipv4 = ipaddress.ip_address(ip)
    netmask = ipaddress.ip_address(netmask)
    netaddr = ipaddress.ip_address(int(ipv4) & int(netmask))
    netaddr = str(netaddr).split('/')[0]
    
    cidr = bin(int(netmask)).count('1')
    print(str(netaddr) + '/' + str(cidr))
    ip_network = ipaddress.ip_network(str(netaddr) + '/' + str(cidr))
    
    return ip_network.hosts()

ip_list = gen_iplist(myip, netmask)

for ip in ip_list:
    pkt = IP(dst=str(ip), ttl=64)/ICMP()
    reply = sr1(pkt, timeout=3)
    
    if reply is not None:
        print(str(ip) + ' is up.')
