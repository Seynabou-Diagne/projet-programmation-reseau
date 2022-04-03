import json
import socket
import mysql.connector 
host= ''
port = 5566
#Script de connection 
def VerificationInfoBd(liste)->list:
    #connexion a la bd
    try:
        #Connexion à la BDD projet avec le username tp et le mot de passe tp
        connexion = mysql.connector.connect(host='localhost', database='projet', user='tp', password='tp')
        curseur = connexion.cursor()
        #Requete permettant de recuperer  les information du client dans la base de donnee
        req = "select * from user where mail = '"+liste[0]+"' and mdp = '"+liste[1]+"'"
        curseur.execute(req)
        resultat = curseur.fetchall()
        return resultat
    except mysql.connector.Error as error:
        print(error)
    finally:
        connexion.close()
 #Script permettant l'inscription d'un client dans la BDD
def Inscription(liste)->bool:
    try:
        connexion = mysql.connector.connect(host='localhost', database='projet', user='tp', password='tp')
        curseur = connexion.cursor()
        #Requete permettant de recuperer d'inserrt du client dans la base de donnee
        req = "insert into user(nom,mail,mdp) values('"+liste[0]+"','"+liste[1]+"','"+liste[3]+"')"
        curseur.execute(req)
        connexion.commit();
        return True
    except mysql.connector.Error as error:
        print(error)
    finally:
        connexion.close()
 #Creation du socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creation de socket
        # Demarrae de server
server.bind((host, port))
print("Demarrage de server....")
while True:
    server.listen(5) #server ecoute sur le port '5566'
    conn, addr = server.accept()

    #On envoi un message
    messagesend = "veillez Choisir une operation à faire "
    messagesend = messagesend.encode("utf8")
    conn.sendall(messagesend)
    print("En attente d'info client")

    #Echange d'info cote server avec client
    messagerecv = conn.recv(1024)  # reception de donne avec param de buffer 1024
    messagerecv = messagerecv.decode("utf8")
    data = json.loads(messagerecv)
    print(data[2])
    if data[2]== "Connexion":
        info = VerificationInfoBd(data)
        print(info)
        if info:
        #Envoi de message de connxion reussi
            messagesend_2 = f"Connexion reussi"
            messagesend_2 = messagesend_2.encode("utf8")
            conn.sendall(messagesend_2)
        else:
                #Envoi de message de connxion echoue
            messagesend_2 = "Identifiant Incorrect"
            messagesend_2 = messagesend_2.encode("utf8")
            conn.sendall(messagesend_2)
            pass
    elif data[2]== "Inscription":
        info = Inscription(data)
        if info:
        #Envoi de message d'inscription reussi
            messagesend_2 = f"Inscription reussi"
            messagesend_2 = messagesend_2.encode("utf8")
            conn.sendall(messagesend_2)
        else:
                #Envoi de message d'echec echoue
            messagesend_2 = "Errreur"
            messagesend_2 = messagesend_2.encode("utf8")
            conn.sendall(messagesend_2)
            pass

conn.close()
server.close()
