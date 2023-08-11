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

# Exo 7 :

class Bouteille:
    def __init__(self, contenance, liquide):
        self.contenance = contenance
        self.liquide = liquide
    
    def boire(self, quantite):
        if quantite <= self.contenance:
            self.contenance -= quantite
            print(f"Vous avez bu {quantite} litres de {self.liquide}. Il reste {self.contenance} litres.")
        else:
            print("La bouteille ne contient pas autant de liquide.")

bouteille1 = Bouteille(1.5, "eau")
bouteille1.boire(0.5)
bouteille1.boire(1.0)

# Exo 8 :
class Banque:
    def __init__(self, titulaire, solde, numero_compte):
        self.titulaire = titulaire
        self.solde = solde
        self.numero_compte = numero_compte
    
    def deposer(self, montant):
        self.solde += montant
        print(f"Montant de {montant}€ déposé. Solde actuel: {self.solde}€")
    
    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"Montant de {montant}€ retiré. Solde actuel: {self.solde}€")
        else:
            print("Solde insuffisant.")
    
    def afficher_solde(self):
        print(f"Solde actuel du compte {self.numero_compte}: {self.solde}€")

compte1 = Banque("Alice", 1000, "123456")
compte1.deposer(500)
compte1.retirer(200)
compte1.afficher_solde()


# Exo 9 :

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def deplacer_horizontal(self, distance):
        self.x += distance
    
    def deplacer_vertical(self, distance):
        self.y += distance
    
    def afficher_coordonnees(self):
        print(f"Coordonnées du point: ({self.x}, {self.y})")

point1 = Point(2, 3)
point1.deplacer_horizontal(5)
point1.deplacer_vertical(-2)
point1.afficher_coordonnees()


# Exo 10 :

def est_palindrome(chaine):
    return chaine == chaine[::-1]

def plus_grand_palindrome(liste):
    palindromes = [mot for mot in liste if est_palindrome(mot)]
    if not palindromes:
        return None
    return max(palindromes, key=len)


# Exo 11 :

# Exo 12 :

# Exo 13 :