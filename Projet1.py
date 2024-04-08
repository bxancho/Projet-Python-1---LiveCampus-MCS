

def connection():
    adresse_IP = input ("Donner l'adresse IP: ")
    nom_utilisateur = input ("Donner le nom d'utilisateur: ")
    return adresse_IP, nom_utilisateur

def choisir_protocole():
    while True:
        protocole = input ("Quel protocole voulez-vous choisir, SSH ou FTP? ").lower() #lower() va convertir la reponse en miniscules, sinon si l'utilisateur écrit le protocole en miniscule et non pas en majuscue on doit obtenir la phrase d'entrer un autre protocole 
        if protocole in ['ssh', 'ftp']:
           return protocole
        else:
            print("Le protocole doit être SSH ou bien FTP, Veuillez réessayer")
def path_fichier():
    path = input("Entrez le path du fichier: ")
    return path

def acceder_password_file(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
             passwords = file.readlines()
    
             passwords = [password.strip() for password in passwords] # Supprimer les espaces vides et les sauts de ligne
             return passwords
    except FileNotFoundError:
        print("fichier non trouvé")        
    
    except OSError:
        print("fichier non accessible")

    except Exception as ex:
        print(f"L'erreur '{ex}' s'est produite")
   

def main():
    adresse_IP, nom_utilisateur = connection()
    print("L'adresse IP est:", adresse_IP)
    print("le nom d'utilisateur est:", nom_utilisateur)

    protocole = choisir_protocole()
    print("Le protocole choisit est: ", protocole)
    
    path = path_fichier()
    acceder_password_file(path)
    common_passwords = acceder_password_file(path)
    if common_passwords:
     print("Liste de mots de passe couramment utilisés :")
     print(common_passwords)  #pour afficher les 10 premiers mots de passe
    else:
     print("Aucune liste de mots de passe récupérée.")
main()

    