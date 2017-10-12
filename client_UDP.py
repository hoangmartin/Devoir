# -*- coding: utf-8 -*-

import socket

#declarer IP, port du client et message

client="192.168.0.202"
port=5005
message="cinema"

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0)
#
sock.connect(client,port)
sock.sendto(message,(client,port))


trameReponse, addr = sock.recvfrom(1024)

print "Réception de la trame de réponse", trameReponse.encode("hex")

code = (ord(b0)<<24)+(ord(b0)<<16)+(ord(b0)<<8)+(ord(b0)<<0)

print code

