##################### Variables globales #####################

couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi','As']
valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}

##################### Classe Carte #####################

class Carte:
    def __init__(self, nom, couleur):
        # Affectation des attributs nom et couleur avec contrôle.
        if nom not in noms :
            assert nom in noms , "Le nom n'est pas bien ecrit."
        else :
            self.nom = nom 
        
        if couleur not in couleurs :
            assert couleur in couleurs , "La couleur n'est pas bien ecrite."
        else :
            self.couleur = couleur

        self.valeur = valeurs[self.nom]

##################### Définition des méthodes d'instances avec contrôle #####################

    def setNom(self, nom): # setter
        self.nom = nom
        self.valeur = valeurs[self.nom]

    def getNom(self): # getter de nom
        return self.nom

    def getCouleur(self): # getter de couleur
        return self.couleur

    def getValeur(self): # getter
        return self.valeur

    def egalite(self, carte):
        if self.valeur == carte.valeur :
            return True
        else :
            return False

##################### Renvoie True si les cartes ont même valeur, False sinon carte: Objet de type Carte #####################

    def estSuperieureA(self, carte):
        if self.valeur > carte.valeur :
            return True 
        else :
            return False

##################### Renvoie True si la valeur de self est supérieure à celle de carte, False sinon carte: Objet de type Carte #####################

    def estInferieureA(self, carte):
        if self.valeur < carte.valeur :
            return True 
        else :
            return False

##################### Teste de la classe Carte #####################

def testCarte():
    valetCoeur = Carte('Valet', 'COEUR',)
    print('Nom:', valetCoeur.getNom())
    print('Couleur:', valetCoeur.getCouleur())
    print('Valeur:', valetCoeur.getValeur())
    valetCoeur.setNom('Dame')
    print('Nom modifie:', valetCoeur.getNom())
    print('Valeur modifiee:', valetCoeur.getValeur())
    # Essai des exceptions: cette instruction conduit à une erreur
    dameCarreau = Carte('Dame', 'COooEUR')

#testCarte()
