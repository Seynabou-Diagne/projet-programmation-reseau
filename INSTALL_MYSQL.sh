#!/bin/bash

### INSTALLATION DES DEPENDANCES POUR L'INSTALLATION DE MYSQL ###

 ## LA MISE A JOUR DU SYSTEME ##
sudo apt update -y
sudo apt upgrade -y

# INSTALLATION DES PACKAGES 

sudo apt-get install mysql-server

# DEMARRAGE DU SERVICE

sudo systemctl start mysql.service

# CONFIGURATION DE MYSQL

sudo mysql
mysql -e 'create database projet';
mysql -e 'show projet';
mysql -e 'create table projet.user(id int,nom varchar(30),mail varchar(30),mdp varchar(20))';

