#!/usr/bin/python3
import ctf_client
import sys
# specify host and ports
host = str(sys.argv[1])
port = sys.argv[2]
if '-' in port:
    port = sys.argv[2].split('-')
    for x in port:
        if x.isdigit:
            x = int(x)
            port_range = [x for x in range(1, x)]
    print(port_range)
            
'''
c = ctf_client.ConnectClass(host, port)
print(f"Preparing to scan {host}:{port}")
c.send_data('hey')
data = c.recv_data()
print(data)
'''
