#coding:utf-8
import json
import socket
import mysql.connector 

def VerificationInfoBd():
    #connexion a la bd
    try:
        connexion = mysql.connector.connect(host='localhost', database='users', user='root', password='root')
        curseur = connexion.cursor()
        req = "select * from user"
        curseur.execute(req)
        resultat = curseur.fetchall()
        return resultat
    except mysql.connector.Error as error:
        print(error)
    finally:
        connexion.close()


host= ''
port = 5566
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creation de socket
        # Demarrae de server
server.bind((host, port))
print("Demarrage de server....")
while True:
    server.listen(5) #server ecoute sur le port '5566'
    conn, addr = server.accept()

    #Demande d'info aux client
    messagesend = "veillez entrer vos identifiants"
    messagesend = messagesend.encode("utf8")
    conn.sendall(messagesend)
    print("En attente d'info client")

    #Echange d'info cote server avec client
    messagerecv = conn.recv(1024)  # reception de donne avec param de buffer 1024
    messagerecv = messagerecv.decode("utf8")
    data = json.loads(messagerecv)

    #verification info
    info = VerificationInfoBd()
    for element in info:
        if element[2] == data[1] and element[3]== data[2]:
            #Envoi de message de connxion reussi
            messagesend_2 = f"Connexion reussi"
            messagesend_2 = messagesend_2.encode("utf8")
            conn.sendall(messagesend_2)
        else:
            # Envoi de message de connxion echoue
            messagesend_2 = f"Identifiant Incorrect"
            messagesend_2 = messagesend_2.encode("utf8")
            conn.sendall(messagesend_2)

conn.close()
server.close()

