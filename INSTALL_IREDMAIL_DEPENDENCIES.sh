#!/bin/bash

### INSTALLATION DES PACKAGES DE IREDMAIL DEPUIS UN DEPOT GITHUB ###

https://github.com/iredmail/iRedMail/archive/refs/tags/1.5.2.tar.gz

## EXTRACT DU FICHIER  ET CD DANS LE DOSSIER

tar xvf 1.5.2.tar.gz
cd iRedMail-1.5.2

## EXECUTION DU SCRIPT IREDMAIL 

# NB: avant l'execution du script le nom de domaine doit etre configuré

# ATTRIBUTION DES DROITS 
chmod +x iRedMail.sh

# EXECUTION SCRIPT

bash iRedMail.sh
