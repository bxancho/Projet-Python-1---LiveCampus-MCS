import requests

class GeoAPI:                                                                                                                               # Classe pour gérer les requêtes à l'API et récupérer les données de localisation
    base_url = "https://geo.api.gouv.fr"                                                                                                    # URL de l'API

    @staticmethod
    def donnees_de_localisation(code):
        url = f"{GeoAPI.base_url}/communes?codePostal={code}" if len(code) == 5 else f"{GeoAPI.base_url}/departements/{code}/communes"      # URL de la requête
        reponse = requests.get(url)                                                                                                         # Envoi de la requête GET à l'URL
        if reponse.status_code == 200:
            return reponse.json()                                                                                                           # Conversion de la réponse en format JSON
        else:
            return None

class InterfaceUtilisateur:                                                                                                                 # Classe pour gérer l'interaction avec l'utilisateur

    @staticmethod
    def utilisateur_input():
        return input("Veuillez saisir un code postal (pour un département ou une ville) : ")

    @staticmethod
    def afficher_population(localisation, population):
        if population is not None:
            print(f"La population pour la zone {localisation} est de {population} habitants.")
        else:
            print("Les informations de population ne sont pas disponibles pour cette zone.")

class MainApp:                                                                                                                              # Classe pour le main

    @staticmethod
    def main():
        user_input = InterfaceUtilisateur.utilisateur_input()                                                                               # Obtention de la donnée rentrer par l'utilisateur
        geo_data = GeoAPI.donnees_de_localisation(user_input)
        if geo_data:
            if len(user_input) == 5:                                                                                                        # Vérification code postal
                population_totale = sum(commune['population'] for commune in geo_data)
                InterfaceUtilisateur.afficher_population(user_input, population_totale)
            elif len(user_input) == 2:                                                                                                      # Vérification code de département
                population_totale = sum(commune['population'] for commune in geo_data)
                InterfaceUtilisateur.afficher_population(user_input, population_totale)
            else:
                print("Code postal ou code de département invalide.")
        else:
            print("Les informations de population ne sont pas disponibles pour cette zone.")


if __name__ == "__main__":                                                                                                                  # Vérification si le script est exécuté en tant que programme principal
    MainApp.main()