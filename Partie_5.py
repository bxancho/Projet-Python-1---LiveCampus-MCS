# Lire un fichier JSON, créer une nouvelle colonne et enregistrer le tout dans un nouveau fichier.

import json

def ajouter_nouvelle_donnee(fichier_entree, fichier_sortie, nom_nouvelle_colonne, donnees_nouvelle_colonne):

    # Lecture du fichier JSON
    with open(fichier_entree, 'r') as fichier_json:
        data = json.load(fichier_json)

    # Ajout de la nouvelle donnée à chaque élément de la liste
    for element in data:
        element[nom_nouvelle_colonne] = donnees_nouvelle_colonne
    
    # Enregistrement dans un nouveau fichier JSON
    with open(fichier_sortie, 'w') as fichier_json:
        json.dump(data, fichier_json)





fichier_entree = r"C:\Users\mikad\Desktop\info_fruit.json"
fichier_sortie = r"C:\Users\mikad\Desktop\info_fruit_nouvelle_colonne.json"
nom_nouvelle_colonne = "Nouvelle Colonne"
donnees_nouvelle_colonne = {'calories': 999, 'fat': 99, 'sugar': 00}

ajouter_nouvelle_donnee(fichier_entree, fichier_sortie, nom_nouvelle_colonne, donnees_nouvelle_colonne)
print(f"Les données ont été exportées vers '{fichier_sortie}' avec succès.")

