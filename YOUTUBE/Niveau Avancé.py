# Les Exercices suivant sont d'un niveau plus avancés :

# Premier Lien : 

# Exo 1 :

def nbCheminsDist(dist):
    if dist == 0:
        return 1
 
    if dist < 0:
        return 0
 
    return nbCheminsDist(dist-1)+nbCheminsDist(dist-2)+nbCheminsDist(dist-3)

# Exo 2 :

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self):
        return self.longueur * self.largeur
    
