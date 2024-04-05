# Créer une archive tar (ou zip) à l’aide de subprocess

import subprocess

def zip_dossier(chemin_dossier, nom_zip, chemin_dossier_export):

    chemin_7z = r"C:\Program Files\7-Zip\7z.exe"
    subprocess.run([chemin_7z, "a", nom_zip, chemin_dossier], cwd=chemin_dossier_export, check=True)        # a correspond à ajouter
    print(f"Compression '{nom_zip}' réussi vers {chemin_dossier_export}.")


chemin_dossier = r"C:\Users\mikad\live-campus-mcs\Exercice_4"
nom_zip = "Exercice_4.zip"
chemin_dossier_export = r"C:\Users\mikad\Desktop" 
zip_dossier(chemin_dossier, nom_zip, chemin_dossier_export)

