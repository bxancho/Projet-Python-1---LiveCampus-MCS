# Reprendre la question 2, et rendez possible le passage d’argument à votre script pour que votre méthode puisse compter le nombre de fichier dans un
# dossier qui sera passé en argument à votre script.

import os
import sys

def compter_fichiers_dans_dossier_donne(chemin_dossier):

    nombre_fichiers = 0
    for entry in os.scandir(chemin_dossier):
        if entry.is_file():                                                  # Vérifier si l'élément est un fichier
            nombre_fichiers += 1
    return nombre_fichiers


if __name__ == "__main__":
    if len(sys.argv) != 2:                                                   # Vérifier s'il y a un argument passé à la ligne de commande
        print("Usage: python script.py <chemin_dossier>")
        sys.exit(1)

chemin_dossier_specifie = sys.argv[1]                                        # Récupérer le chemin du dossier passé en argument
if not os.path.exists(chemin_dossier_specifie):
    print("Le dossier spécifié n'existe pas.")
    sys.exit(1)

nombre_fichiers = compter_fichiers_dans_dossier_donne(chemin_dossier_specifie)
print("Nombre de fichiers dans le dossier spécifié:", nombre_fichiers)

#                                                                              python C:\Users\mikad\live-campus-mcs\Exercice_4\Partie_3.py C:\Users\mikad\live-campus-mcs\Exercice_4\
# python Exercice_4\Partie_3.py C:\Users\mikad\live-campus-mcs\Exercice_3\
