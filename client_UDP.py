# -*- coding: utf-8 -*-

import socket

#je declare IP, port du client et message

client="192.168.0.202"
port=5005
message="cinema"
#j'ouvre une socket UDP / IP, en IP V4
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0)
#j'envoie le message au serveur
sock.connect((client,port))
sock.sendto(message,(client,port))

#je récupère des requêtes
trameReponse, addr = sock.recvfrom(1024)
#afficher l'ID de trame de reponse
print "Réception de la trame de réponse", trameReponse.encode("hex")

#je récupère le code
#ord retourne la valeur hex en caractère
#je décale les octets
code = (ord(trameReponse[0]))+(ord(trameReponse[1])<<8)+(ord(trameReponse[2])<<16)+(ord(trameReponse[3])<<24)
print code

#numéro ciné: 4158522552
