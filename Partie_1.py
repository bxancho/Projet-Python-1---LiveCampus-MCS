#A l’aide de la méthode de votre choix, créer une méthode pour lister le contenu de votre dossier de travail et créer une copie du fichier de votre choix ; 
# dans le nom de cette copie devra figurer la date et l’heure à laquelle la copiea été faite

import os
import shutil
from datetime import datetime

def lister_contenu_dossier():

    chemin_dossier = os.getcwd()                                                                              # Récupérer le chemin absolu du dossier de travail
    contenu_dossier = os.listdir(chemin_dossier)                                                              # Afficher le contenu du dossier de travail
    print("Contenu du dossier :")
    for element in contenu_dossier:
        print(element)

def copier_fichier_avec_date(nom_fichier_source):
    
    if os.path.exists(nom_fichier_source):                                                                    # Vérifier si le fichier source existe dans le dossier
        nom_fichier, extension = os.path.splitext(nom_fichier_source)                                         # Séparer le nom de fichier et l'extension
        date_heure = datetime.now().strftime("%d-%m-%Y")                                                      # Obtenir la date et l'heure actuelles
        nom_fichier_copie = f"{nom_fichier}_{date_heure}{extension}"                                          # Construire le nouveau nom de fichier avec la date et l'heure
        shutil.copy(nom_fichier_source, nom_fichier_copie)                                                    # Copier le fichier source avec le nouveau nom
        print(f"Le fichier {nom_fichier_source} a été copié avec succès en tant que {nom_fichier_copie}.")
    else:
        print(f"Le fichier {nom_fichier_source} n'existe pas dans le dossier.")



lister_contenu_dossier()

nom_fichier_source = r"C:\Users\mikad\live-campus-mcs\Exercice_4\Partie_1.py"
copier_fichier_avec_date(nom_fichier_source)
