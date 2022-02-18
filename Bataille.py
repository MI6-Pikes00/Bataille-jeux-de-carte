
##################### Importation des fichiers néccecaires au fonctionnement #####################

from Joueur import *
from JeuCartes import *
from Carte import *

##################### Classe Bataille #####################

class Bataille:

##################### L'initialisation va créer les 2 joueurs, mélanger et distribuer les cartes #####################

    def __init__(self, nomJ1, nomJ2, tailleJeuCartes,):
        self.J1 = Joueur(nomJ1)
        self.J2 = Joueur(nomJ2) # valeur par défaut qui sera modifiée
        self.jeuCartes = JeuCartes(tailleJeuCartes) # valeur par défaut qui sera modifiée
        paquet_jeux = self.jeuCartes.distribuerJeu(2,int(tailleJeuCartes/2))# Selecteur suivant nombre de cart 32 ou 52
        self.J1.setMain(paquet_jeux[0])
        self.J2.setMain(paquet_jeux[1])

        ## On mélange le jeu et on le distribue aux 2 joueurs
 
##################### Fonction jouer qui permet le jeux #####################

    def jouer(self):
        print("Que le meilleurs gagne !")
        print("Début de la partie")
        tour = 0
        e = 0
        pile1= []
        pile2= []

##################### Boucle principale qui répete le jeux tant qu'un des joueurs a encore des cartes ##################### 

        while self.J1.getNbCartes() != 0 and self.J2.getNbCartes() != 0 :
            print(" ")
            tour += 1
            e += 1
            print ("------------------ Tour de carte n°",tour, "------------------")

            if e == 32 :
                self.J1.melangerMain()
                self.J2.melangerMain()
                e = 0
                
##################### Chaque Joueur joue ca carte #####################

            pile1.append(self.J1.jouerCarte())
            print("Carte jouée par", self.J1.getNom(), ":" , pile1[-1].getNom(), "de" ,pile1[-1].getCouleur())
            pile2.append(self.J2.jouerCarte())
            print("Carte jouée par", self.J2.getNom(), ":" , pile2[-1].getNom(), "de" ,pile2[-1].getCouleur())


##################### Cas d'égalité entre les joueurs #####################

            while pile1[-1].egalite(pile2[-1]):
                print ("------------------ EGALITÉ ------------------")
                for i in range (2):
                    pile1.append(self.J1.jouerCarte())
                    pile2.append(self.J2.jouerCarte())
                
                if pile1[-1] == None or pile2[-1] == None :
                    print ("Un des joueurs n'as plus assez de carte !")
                    break                
                
                print("Carte jouée par", self.J1.getNom(), ":" , pile1[-1].getNom(), "de" ,pile1[-1].getCouleur())
                print("Carte jouée par", self.J2.getNom(), ":" , pile2[-1].getNom(), "de" ,pile2[-1].getCouleur())

            if pile1[-1] == None or pile2[-1] == None :
                break

##################### Cas où la carte du joueur 1 est supérieur à celle du joueur 2 #####################

            elif pile1[-1].estSuperieureA(pile2[-1]):
                for i in range(len(pile1)):
                    self.J1.insererMain(pile1.pop())
                for i in range(len(pile2)):
                    self.J1.insererMain(pile2.pop())
                print("Le vainqueur de la manche est", self.J1.getNom())

##################### Cas où la carte du joueur 1 est inférieur à celle du joueur 2 #####################

            elif pile1[-1].estInferieureA(pile2[-1]):
                for i in range(len(pile1)):
                    self.J2.insererMain(pile1.pop())
                for i in range(len(pile2)):
                    self.J2.insererMain(pile2.pop())
                print("Le vainqueur de la manche est", self.J2.getNom())

##################### Fin grande boucle while #####################

            print("Nombre de carte de", self.J1.getNom(), ":", self.J1.getNbCartes())
            print("Nombre de carte de", self.J2.getNom(), ":", self.J2.getNbCartes())

##################### Impression des résultats suivant le nombre de carte ##################### 

        if self.J1.getNbCartes() > self.J2.getNbCartes() :
            print("Le grand vainqueur est ", self.J1.getNom())
            print("avec",self.J1.getNbCartes(), "cartes !")
        elif self.J1.getNbCartes() < self.J2.getNbCartes() :
            print("Le grand vainqueur est ", self.J2.getNom())
            print("avec",self.J2.getNbCartes(), "cartes !")

##################### Tester la classe Bataille sans le fichier main.py #####################
def testBataille():
    Bataille("Momo", "Titi", 52).jouer()
