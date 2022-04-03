# projet-programmation-reseau
Le but du projet est de pouvoir mettre en place un dispositif permettant 
d’analyser un packet. L’analyse mettra en évidence la compréhension de 
l’encapsulation des données et de l’utilisation des bibliothèques adéquates 
pour le faire. Il sera aussi mis en évidence une maitrise assez minimaliste de la 
programmation shell.

* Le script INSTALL_MYSQL.sh

Ce script permet l'installation des dépendances de mysql ainsi qu'à la fin la configuration 
du serveur mysql avec la creation de la base de donnée et de la table user 
Lancer le script avec ./INSTALL_MYSQL.sh

* Le script INSTALL_IREDMAIL_DEPENDENCIES.sh

Ce script permet l'installation des dépendances de iRedMail ainsi la configuration
Lancer le script avec ./INSTALL_IREDMAIL.DEPENDENCIES.sh

* Le script INSTALL_ALL_DEPENDENCIES.sh


Ce script permet d'executer simultanément les deux scripts précédents.
Lancer le script avec ./INSTALL_ALL_DEPENDENCIES.sh

* Le script server.py

Ce script s'execute du côté de la machine serveur.
Il permet les operation au niveau de la bdd en fonction du choix du client
Si le client choisi de se connecter , le script prendra en entrée les informations saisies par le client(nom et mot de passe) , et verifiera si le client existe dans la base de données. Un message est renvoyé pour notifier au client si la connexion est reussi ou pas.
Si le client choisi de s'inscrire , le script prendra en entrée les informations saisies par le client(nom,mail et mot de passe) et les ajoute dans la base de donnée.
Executer le script avec la version 3 de python
NB: le plugins mysql-connector est nécessaire , pour l'installer il faut executer la commande :
-python3 -m install mysql-connector

Commmande pour executer le script : python3 server.py

* Le script client.py

Ce script s'execute du coté de la machine client , pour le lancer il faudrait au préalable lancer le script du serveur
Il permet au client de se connecter ou de creer un compte à travers un menu de choix qu'il propose à l'utilisateuur


Commmande pour executer le script : python3 client.py
