#coding:utf-8
import socket
import json


host= '192.168.10.1'
port = 5566


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creation de socket
try:
    client.connect((host, port))  # Connexion au server
    #Echange d'info avec le server cote client
    data = client.recv(1024)
    data = data.decode("utf8")
    print(data)

    clientInfo = []  # variable dinfo client
    nom = input("Entrer votre nom svp :")
    mail = input("Entrer votre address mail :")
    mdp = input("Entrer votre mdp :")
    clientInfo.append(nom)
    clientInfo.append(mail)
    clientInfo.append(mdp)
    messagesend = json.dumps(clientInfo)
    messagesend = messagesend.encode("utf8")
    client.sendall(messagesend)

    data = client.recv(1024)
    data = data.decode("utf8")
    print(data)

except Exception as e:
    print(e)
finally:
    client.close()


