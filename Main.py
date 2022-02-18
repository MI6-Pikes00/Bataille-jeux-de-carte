##################### Importation des fichiers néccecaires au fonctionnement #####################

from Bataille import *

##################### Fonction principale qui permet de jouer #####################
def main() :

##################### Laisse le choix des noms des joueurs et du nombre de carte #####################

    print('Veuillez entrer le nom du joueur 1 : ',)
    P1 = str(input())
    print('Veuillez entrer le nom du joueur 2 : ')
    P2 = str(input())
    
    nbCarte=int(input("Choisir entre 32 et 52 cartes :"))

    Bataille(P1, P2, nbCarte).jouer()
    
main()

  


