#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:38:24 2017

@author: aj
"""

import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:

	sockets_list = [sys.stdin, server]

	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

	for socks in read_sockets:
		if socks == server:
			message = socks.recv(2048).decode()
			print (message)
		else:
			message = sys.stdin.readline()
			server.send(message.encode())
			sys.stdout.write("<You>")
			sys.stdout.write(message)
			sys.stdout.flush()
	if message.lower().strip() == 'bye':
		break
print("closing the connection")
server.close()




