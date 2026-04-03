# Principe de Programmation (PP) - Master 1 Informatique
Université Sorbonne Paris Nord

Ce dépôt contient les cours et TPs du module Principe de Programmation.
Les dossiers sont organisés sous la forme CMn/TPn où n est le numéro de la séance.

---

## Structure du projet

PP/
├── CM2/          # API REST Python
├── CM3/          # REST PHP + MVC
├── TP1/          # SOAP Java
├── TP4/API+DAD/  # REST PHP + MySQL
└── DockerTP/     # Docker

---

## Contenu des séances

### CM2 - API REST Python
- Utilisation des méthodes REST : GET, POST...
- Initiation au logiciel Postman
- rest.py : initiation et entraînement avec le prof
- APICamions.py : fichier personnel avec les méthodes count_camion() et count_camion_annee(annee)

---

### TP1 - SOAP Java
- Cours sur le protocole SOAP en Java
- Rapport : /TP1/Rapport TP1.pdf

---

### CM3 - REST PHP (20/02/2026)
- REST en PHP
- Création progressive d'une architecture MVC

---

### CM4/TP4 - REST PHP + MySQL (27/02/2026)
- Test REST PHP avec serveur MySQL

Guide de lancement :
1. Lancer MySQL via XAMPP
2. Lancer l'API : TP4/API+DAD
3. Lancer l'application PHP (connexion automatique à l'API)

---

### CM5/CM6 - Docker

Un Dockerfile sert à automatiser la création d'images Docker.
Il installe automatiquement les paquets nécessaires dans une image réutilisable.

Lancer un conteneur simple (Alpine) :

mkdir monapp
cd monapp
Set-Content Dockerfile "FROM alpine:latest`nCMD echo 'Bonjour HR'"
docker build -t monapp .
docker run monapp


Lancer une application Java avec Docker :

1. Créer le fichier Java

New-Item -Name "Main.java" -ItemType File
notepad Main.java

public class Main {
    public static void main(String[] args) {
        System.out.println("Bonjour HR");
    }
}

2. Créer le Dockerfile

@"
FROM openjdk:17
WORKDIR /app
COPY Main.java .
RUN javac Main.java
CMD ["java", "Main"]
"@ | Set-Content Dockerfile

3. Build et lancer

docker build -t monapp .
docker run monapp

---

## Technologies utilisées
- Python, PHP, Java
- Docker, MySQL, XAMPP
- REST, SOAP, MVC
- Postman

---

Master 1 Informatique - Sorbonne Paris Nord