# Save as client.py 
# Message Sender
import os
import random
import time
from socket import *
print ("""
Press any of the key to make connection with that Social networking site
Press 1: Facebook
Press 2: Twitter
Press 3: Instagram
""")

a=raw_input("Waiting for the input--")
if int (a)==1:
    time.sleep(3)
    print ("""
    Connection Established with Facebook
    Now you can send any message to any friend on Facebook""")    

if int (a)==2:
    time.sleep(3)
    print ("""
    Connection Established with Twitter
    Now you can send any message to any friend on Twitter""")
    
if int (a)==3:
    time.sleep(3)
    print ("""
    Connection Established with Instagram
    Now you can send any message to any friend on Instagram""")     


host = "127.0.0.1" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = raw_input("Enter message to send or type 'exit': ")
    UDPSock.sendto(data, addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)
