# A l’aide de la méthode de votre choix, compter le nombre de fichier (pas dossier !) dans votre dossier de travail

import os

def nombre_fichiers_dans_dossier():

    chemin_dossier = os.getcwd()                                                    # Récupérer le chemin absolu du dossier
    nombre_fichiers = 0                                                             
    for element in os.listdir(chemin_dossier):                                      # Parcourir tous les éléments du dossier
        if os.path.isfile(os.path.join(chemin_dossier, element)):                   # Vérifier si l'élément est un fichier
            nombre_fichiers += 1
    return nombre_fichiers


nombre_fichiers = nombre_fichiers_dans_dossier()
print("Nombre de fichiers dans le dossier : ", nombre_fichiers)

