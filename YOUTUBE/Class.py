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
    
# Exo 3 :

import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def aire(self):
        return math.pi * self.rayon ** 2
    
# Exo 4 :

class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    
    def presentation(self):
        return f"Je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans."

# Exo 5 :

class Chien:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def aboyer(self):
        print(f"Woof! Je m'appelle {self.nom}.")

# Exo 6 :

class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
    
    def informations(self):
        return f"Titre: {self.titre}, Auteur: {self.auteur}, Année: {self.annee}"
