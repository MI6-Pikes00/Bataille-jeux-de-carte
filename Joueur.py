##################### Importation des fichiers néccecaires au fonctionnement #####################

from JeuCartes import *
from random import shuffle

class Joueur:
    def __init__(self, nom):
        # On peut imaginer que lors de la création du joueur, ce dernier n'a pas encore de carte.
        self.nom = nom
        self.nbCartes = 0 # valeur par défaut qui sera modifiée
        self.mainJoueur = []  # valeur par défaut qui sera modifiée
 
    def setMain(self,listeCartes):
        ''' Initialise la main du joueur avec la liste des cartes donnée comme paramètre d’entrée '''
        self.mainJoueur = listeCartes
        self.nbCartes= self.nbCartes + len(self.mainJoueur)
 
    def getNom(self):
        '''Accesseur de l’attribut nom '''
        return self.nom
 
    def getNbCartes(self):
        '''Accesseur de l’attribut nbCartes'''
        return self.nbCartes
 
    def jouerCarte(self):
        '''Enlève et renvoie la dernière carte du dessus (objet de type Carte) de la main du joueur,
         ou retourne None s’il n’y a plus de cartes dans la main du joueur'''

        if self.getNbCartes() != 0:
            derniereCarte = self.mainJoueur.pop()
            self.nbCartes = self.nbCartes - 1
            return derniereCarte
        else:
            return None
 
    def insererMain(self,CartesGagnees):
        ''' Méthode qui insère des cartes dans la main du Joueur « en dessous »'''
        self.mainJoueur.insert(0,CartesGagnees)
        self.nbCartes = self.nbCartes +1

    def melangerMain(self):

        random.shuffle(self.mainJoueur)


####################################################################
################## FAIRE LES FONCTIONS TEST JOEUR ##################
####################################################################

def testJoueur():

    jeu32 = JeuCartes(32)
    jeu32.melanger()
    toto = Joueur("Toto")
    toto.setMain(jeu32.distribuerJeu(1,32)[0])
    print(toto.getNom())
    print(toto.getNbCartes())
    print(toto.jouerCarte())
    print(toto.insererMain(Carte("As", "PIQUE")))

