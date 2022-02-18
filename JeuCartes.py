##################### Importation des fichiers néccecaires au fonctionnement #####################

from Carte import * # Il faut importer la classe Carte et les variables globales
import random # Nécessaire pour mélanger le jeu

##################### Classe JeuCartes #####################
class JeuCartes:
    def __init__(self, nbCartes=52):
        # Le jeu doit comporter 32 ou 52 cartes, effectuer un contrôle (faire un assert entre 32 et 52)
        assert nbCartes == 52 or nbCartes == 32, "Taille du jeux cartes ne corespond pas a 52 ou 32"
        self.nbCartes = nbCartes
        self.jeu = [] # self.jeu est une liste des self.nbCartes
        self.creerJeu()
        self.melanger()

################# Définition des méthodes d'instances #####################
    def getTailleJeu(self):

        ''' Fonction qui retourne le nombre de cartes du jeu
        Valeur retournée: type int '''

        return self.nbCartes


    def creerJeu(self): # utilise des objet
        
        '''Créée la liste des cartes de l'attribut self.jeu '''
        
        for couleur in couleurs:
            for nom in noms:
                if self.nbCartes == 32 and nom not in ['2','3','4','5','6']:
                    self.jeu.append(Carte(nom, couleur))
                if self.nbCartes == 52:
                    self.jeu.append(Carte(nom, couleur))
                  
    def getJeu(self):
        '''Renvoie la liste des cartes correspondant à l'attribut self.jeu'''

        return self.jeu

    def melanger(self): # utiliser le module random ...

        '''Mélange sur place les cartes de la liste des cartes associée
        au champ self.jeu'''

        random.shuffle(self.jeu) 

    def distribuerCarte(self):

        ''' Cette fonction permet de distribuer une carte à un joueur.
            Elle retourne la carte Valeur retournée: Objet de type Carte '''

        return self.jeu.pop()

    def distribuerJeu(self, nbJoueurs, nbCartes):

        ''' Cette méthode distribue nbCartes à chacun des nbJoueurs, ... '''

        assert nbJoueurs*nbCartes<=self.nbCartes, "Pas assez de cartes dans le jeu"
        paquet=[]
        for i in range(nbJoueurs):
            paquetJoueur = []
            for x in range(nbCartes):
                paquetJoueur.append(self.distribuerCarte())
            paquet.append(paquetJoueur)
        return paquet
       
##################### Fonction test et vérification de la classe JeuCartes #####################
def testJeuCartes():
    jeu52 = JeuCartes(52)
    jeu52.melanger()
    L=jeu52.getJeu()
    carte= L[3] # le 3e carte
    print('Nom:', carte.getNom())
    print('Couleur:', carte.getCouleur())
    print('Valeur:', carte.getValeur())
    # Distribution de 4 cartes à 3 joueurs
    distribution_3j_4c = jeu52.distribuerJeu(3, 4)
    for i in range(3):
        print('Joueur', i+1, ':')
        listeCartes = distribution_3j_4c[i]
        for c in listeCartes:
            print(c.getNom(), 'de', c.getCouleur())
   # Distribution de 10 cartes à 6 joueurs pour générer une exception (6X10 > 52)
    distribution_6_joueurs_10_cartes_par_joueur = jeu52.distribuerJeu(6, 10)

#testJeuCartes()