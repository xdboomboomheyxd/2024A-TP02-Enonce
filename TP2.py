"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 02
Numéro d'équipe :  10
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv



csvfile = open('collection_bibliotheque.csv')
dictionnaire = csv.reader(csvfile)

bibliotheque={}

for row in dictionnaire:
    bibliotheque[row[3]]=(row[0],row[1],row[2])
del bibliotheque['cote_rangement']
csvfile.close()

print(f' \n Bibliotheque initiale : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici






########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






