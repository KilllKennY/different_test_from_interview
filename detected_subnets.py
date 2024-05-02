#!/usr/bin/env python3
import ipaddress
import re
import sys

DEFAULT_INTERNAL_SUBNETS = ['10.254.196.0/24',]
DEFAULT_EXTERNAL_SUBNETS = ['87.250.247.0/24',]
INTERNAL_SUBNETS_FILE = 'internal_subnets.txt'
EXTERNAL_SUBNETS_FILE = 'external_subnets.txt'

ip_subnets = {"internal": [], "external": [],}

def configure_subnets():
    if INTERNAL_SUBNETS_FILE or EXTERNAL_SUBNETS_FILE:
        with open('INTERNAL_SUBNETS_FILE', 'r') as file:
            int_subnets = file.split('\n')
            ip_subnets["internal"].extend(int_subnets)
        with open('EXTERNAL_SUBNETS_FILE', 'r') as file:
            ext_subnets = file.split('\n')
            ip_subnets["external"].extend(ext_subnets)
    ip_subnets["internal"].extend(DEFAULT_INTERNAL_SUBNETS)  
    ip_subnets["external"].extend(DEFAULT_EXTERNAL_SUBNETS)  

def get_ip_subnet_type(ip):
    subnet_type = 'unknown'
    for ip_subnet in ip_subnets['internal']:
        if ipaddress.ip_address(ip) in ipaddress.ip_network(ip_subnet):
            subnet_type = 'internal'
    for ip_subnet in ip_subnets['external']:
        if ipaddress.ip_address(ip) in ipaddress.ip_network(ip_subnet):
            subnet_type = 'internal'
    return subnet_type

def main():
    configure_subnets()
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        else:
            fields = line.split()
            ips = re.findall("www\.[A-za-z]+\.[a-z]+\s+\:\s+(.*$)", fields, flags=re.MULTILINE)
            subnet_type = get_ip_subnet_type(fields[4])
            output_string = ""
            for field in fields:
                output_string += field + " "
            output_string += subnet_type
            print(output_string)

if (__name__ == "__main__"):
    sys.exit(main())


with open('sample.log', 'r') as infile:
    main(infile)
    
