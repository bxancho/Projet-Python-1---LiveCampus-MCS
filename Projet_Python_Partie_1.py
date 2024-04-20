import requests

class GeoAPI:                                                               # Classe pour gérer les requêtes à l'API et récupérer les données de localisation

    base_url = "https://geo.api.gouv.fr"                                    # URL de l'API

    @staticmethod                                  
    def donnees_de_localisation(localisation):
        url = f"{GeoAPI.base_url}/communes?codePostal={localisation}"             # URL de la requête
        reponse = requests.get(url)                                         # Envoi de la requête GET à l'URL
        if reponse.status_code == 200:                                      # Vérification du code de statut de la réponse
            return reponse.json()                                           # Conversion de la réponse en format JSON
        else:
            return None


class Population:                                                           # Classe pour extraire la population à partir des données de localisation
    @staticmethod                                 
    def extraire_population(donnees_localisation):          
        if donnees_localisation:                                            # Vérification de la présence de l'argument
            population = donnees_localisation[0]['population']              # Extraction de la population à partir des données et renvoi
            return population
        else:
            return None

class InterfaceUtilisateur:                                                 # Classe pour gérer l'interaction avec l'utilisateur

    @staticmethod
    def utilisateur_input():
        return input("Veuillez saisir un département ou une ville (code postal) : ")

    @staticmethod
    def afficher_population(localisation, population):
        if population:
            print(f"La population de la zone {localisation} est de {population} habitants.")
        else:
            print("Les informations de population ne sont pas disponibles pour cette zone.")

class MainApp:                                                              # Classe pour exécuter le programme principal

    @staticmethod
    def main():
        user_input = InterfaceUtilisateur.utilisateur_input()                                      # Obtention de l'entrée de l'utilisateur
        donnees_localisation = GeoAPI.donnees_de_localisation(user_input)                   # Récupération des données de localisation en fonction de l'entrée
        population = Population.extraire_population(donnees_localisation)            # Extraction de la population à partir des données de localisation
        InterfaceUtilisateur.afficher_population(user_input, population)                           # Affichage de la population


if __name__ == "__main__":                                  # Vérification si le script est exécuté en tant que programme principal
    MainApp.main()
