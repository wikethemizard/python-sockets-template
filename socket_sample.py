#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' #Must be str.
PORT = 7777 #Must be int.

#The socket object has a socket function that you provide the AF_INET and SOCK_STREAM to.
#AF_INET is ipv4.
#SOCK_STREAM is a port.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print ("[+] Connecting to target...")
    #Connect to the defined IP and Port.
    s.connect((HOST, PORT))

    #Receive any data provided by outgoing port. Note: If no response given script hangs.
    #print ("[+] Receiving data (if response given)...")
    #data=s.recv(1024)

    #print ("[+] Response:")
    #print (data)

    #Send data in python2:
    #buffer = "\x41\x42\x43\x44"
    #print ("[+] Sending buffer...")
    #s.send(buffer)

    #Send data in python3:
    buffer = "Hello? Do you guys have mics?\n"
    print ("[+] Sending buffer...")
    s.sendto(buffer.encode(), (HOST, PORT))

    print ("[+] Done! Exiting...")
except:
    print("[!] Could not connect to target...")
