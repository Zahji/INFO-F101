# https://www.youtube.com/watch?v=iNeqb-URBj4&ab_channel=Foxxpy-Mathématiquesetalgorithmie

#001 Nombre premier ?
    
def is_prime(n):
    for d in range(2,n):
        if n % d == 0:
            return False
    return True

#002 Nombres premiers dans un intervalle ?

def is_prime(n):
    for d in range(2,n):
        if n % d == 0:
            return False
    return True

def get_primes_list(inf, sup):
    primes_list = []
    for nbr in range(inf, sup+1):
        if is_prime(nbr):
            primes_list.append(nbr)
    return primes_list

#003 Nombre Parfait ?

def get_dividers(n):
    dividers_list = []
    for divider in range(1, n+1):
        if n % divider == 0:
            dividers_list.append(divider)
    return dividers_list

def is_perfect(nb):
    if sum(get_dividers(nb)[:-1]) == nb:
        return True
    else:
        return False

#004 Nombre Parfait dans un intervalle ?

def get_dividers(n):
    dividers_list = []
    for divider in range(1, n+1):
        if n % divider == 0:
            dividers_list.append(divider)
    return dividers_list

def is_perfect(nb):
    if sum(get_dividers(nb)[:-1]) == nb:
        return True
    else:
        return False

def get_perfects_list(inf, sup):
    perfects_list = []
    for nbr in range(inf, sup+1):
        if is_perfect(nbr):
            perfects_list.append(nbr)
    return perfects_list

#005 Valeur Factorielle ?

def factorial(nb):
    if nb == 0 or nb == 1:
        return 1
    product = 1
    for num in range(1, nb+1):
        product = product * num
    return product

#006 Nombre spy ?

from math import prod
def spy_number(n):
    sum_n = sum(map(int, list(str(n))))
    product_n = prod(map(int, list(str(n))))
    return sum_n == product_n

#007 Complément d'un Nombre ?

def cmplt(number):
    if isinstance(number,int):
        number = bin(number)
    if "0b" in number:
        number = number.replace("0b", "")

    new_number = ""
    for bit in number:
        if bit == "0":
            new_number += "1"
        else:
            new_number += "0"
    return new_number

#008 Conversion Temps ?

def convert_seconds(seconde):
    heure = seconde // 3600
    seconde = seconde - 3600 * heure
    minute = seconde // 60
    seconde = seconde - 60 *minute
    return heure, minute, seconde

#009 Nombre décimal en binaire ?

def convert_binaire(n):
    resultat = []
    while n >= 1:
        reste = n % 2
        n = n // 2
        resultat.append(reste)
    resultat.reverse()
    return "".join(map(str, resultat))

#010 Nombre binaire en décimal ?

def binary_to_decimal(n):
    if "0b" in n:
        n = n.replace("0b", "")
    total = 0
    for i, bit in enumerate(n[::-1]):
        total += int(bit) * 2**i
    return total

#011 Traduire du Morse ?

def word_to_morse(word):
     code = { "a" : ".-",
             "b" : "-...",
             "c" : "-.-.",
             "d" : "-..",
             "e" : ".",
             "f" : "..-.",
             "g" : "--.",
             "h" : "....",
             "i" : "..",
             "j" : ".---",
             "k" : "-.-",
             "l" : ".-..",
             "m" : "--",
             "n" : "-.",
             "o" : "---",
             "p" : ".--.",
             "q" : "--.-",
             "r" : ".-.",
             "s" : "...",
             "t" : "-",
             "u" : "..-",
             "v" : "...-",
             "w" : ".--",
             "x" : "-..-",
             "y" : "-.--",
             "z" : "--..",
             "1" : ".----",
             "2" : "..---",
             "3" : "...--",
             "4" : "....-",
             "5" : ".....",
             "6" : "-....",
             "7" : "--...",
             "8" : "---..",
             "9" : "----.",
             "0" : "-----"
        }
     morse_word = []
     for char in word:
          morse_word.append(code[char.lower()])
     return " ".join(morse_word)
     
#012 Traduire en Morse ?

def string_to_word(string):
     string = string.split(" ")
     morse_string = []
     for word in string:
          morse_string.append(word_to_morse(word))
     return " ".join(morse_string)

#013 Inverser un mot ?

def reverse(word):
    nv_mot = ""
    for lettre in word:
        nv_mot = lettre + nv_mot
    return nv_mot

#014 Fontion Len() ?

def length(liste):
    total = 0
    for element in liste:
        total += 1
    return total

#015 Anagrammes ?

def anagrame(word1, word2):
    if len(word1) != len(word2):
        return False
    if sorted(word1.upper()) == sorted(word2.upper()):
        return True
    else:
        return False

#016 Fibonacci ?

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#017 Nombre Triangulaire ?

def triangulaire(n):
    total = 0
    for i in range(1, n+1):
        total += 1
    return total

#018 Nombre Triangulaire Formule ?

def triangulaire_formule(n):
    return (n*(n+1))/2

#019 Diviseurs d'un Nombre ? 

def get_dividers(n):
    dividers_list = []
    for divider in range(1, n+1):
        if n % divider == 0:
            dividers_list.append(divider)
    return dividers_list

#020 Nombre puissance d'un autre Nombre ?

def is_power(n, p):
    for i in range(1,n):
        if i**p > n:
            return False
        elif i**p == n:
            return True
        
#021 Puissance d'un nombre ?

def power(n,p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        total = 1
        for i in range(p):
            total *= n
            return total
        
#022 Somme Puissance ?

def sum_power(n, k):
    total = 0
    for i in range(k+1):
        total = total + n ** i
    return total

#023 Identité Remarquable ?

def identite1(a, b):
    return (a+b)**2

def identite2(a,b):
    x = a**2
    y = 2*a*b
    z = b**2
    return x, y, z

#024 Somme de Nombres Binaires ?
 
def somme_binaire(binaire1, binaire2):
    if "0b" in binaire1:
        binaire1 = binaire1.replace("0b", "")
    if "0b" in binaire2:
        binaire2 = binaire2.replace("0b", "")
    somme = int(binaire1, 2) + int(binaire2, 2)
    return bin(somme)

#025 Triangle Pascal ?

def triangle_pascal(n):
    if n == 0:
        return []
    pascal = [[1]]
    for i in range(1,n):
        line = [1]
        for j in range(len(pascal)):
            if j+1 < len(pascal):
                line.append(pascal[i-1][j] + pascal[i-1][j+1])
        line.append(1)
        pascal.append(line)
    return pascal

#026 Polynome second degré ?

from math import *
def discriminant(a,b,c):
    return b**2 - 4*a*c

def polynome(a,b,c):
    delta = discriminant(a,b,c)
    if delta < 0:
        return None, None
    elif delta == 0:
        return -b / (2*a), None
    else:
        x1 = (-b+sqrt(delta))/2*a
        x2 = (-b-sqrt(delta))/2*a
        return x1, x2
    
#027 Coefficient Binomial ?

from math import factorial
def binomial(n, k):
    return  factorial(n)/factorial(k)*factorial(n-k)

#028 PGCD ?

def pgcd(x,y):
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    for k in range(y//2, 0, -1):
        if x % k == 0 and y % k == 0:
            return k
        

#029 Moyenne Arithmérique ?

def moyenne_arithmetique(liste):
    return (1/len(liste)) * sum(liste)

#030 Moyenne Harmonique ?

def harmonique(liste):
    sum_liste = 0
    for nb in liste:
        sum_liste += (1/nb)
    return len(liste) / sum_liste

#031 Moyenne Quadratique ?

from math import *
def quadratique(liste):
    sum_liste = 0
    for nb in liste:
        sum_liste += nb**2
    return sqrt(sum_liste/len(liste))

#032 Moyenne ?

from math import *
def moyenne(liste):
    return (1/len(liste)) * sum(liste)

#033 Variance ?

def variance(liste):
    moy = moyenne(liste)
    var = 0
    for nb in liste:
        var += (nb - moy)**2
    return var / len(liste)

#034 Ecart Type ?

def ecart_type(liste):
    moy = moyenne(liste)
    var = 0
    for nb in liste:
        var += (nb - moy)**2
    return sqrt(var/len(liste))

#035 Concatener 2 listes ?

def concatenate(liste1, liste2):
    new_list = list()
    for liste in [liste1, liste2]:
        for element in liste:
            new_list.append(element)
    return new_list

#036 Générer une matrice aléatoire ?

from random import randint

def afficher_matrice(matrice):
    for line in matrice:
        print(line)

        

def generer_matrice_aleatoire(M, N, inf=1, sup=100):
    matrix = []
    for i in range(M):
        line = []
        for j in range(N):
            line.append(randint(inf, sup))
        matrix.append(line)
    return matrix

#037 Vérifier que tous les éléments d'une liste sont différents ?

def elements_uniques(liste):
    if len(liste) == len(list(set(liste))):
        return True
    else:
        return False
#038 Mélanger les caractères d'une chaîne de caractères ?

from random import randint, shuffle

def shuffle_string(string):
   new_string = ""
   while(len(string) > 0):
        random_digit = randint(0, len(string)-1)
        new_string += string[random_digit]
        string = string[:random_digit] + string[random_digit+1:]
   return new_string

def shuffle_string_2(string):
    liste = list(string)
    shuffle(liste)
    return "".join(liste)

#040 Matrice Nullle ?

def matrice_nulle(M, N):
    matrice = []
    for i in range(M):
        matrice.append([0 for x in range(N)])
    return matrice

#041 Produit Scalaire ?

def transpose(matrix):
    result_matrix = []
    for col in range(len(matrix[0])):
        line_matrix = []
        for line in range(len(matrix)):
            line_matrix.append(matrix[line][col])
        result_matrix.append(line_matrix)
    return result_matrix



def produit_scalaire(A, B):
    if len(A[0]) != len(B):
        return None
    result_matrix = []
    for line in A:
        line_matrix = []
        for col_B in transpose(B):
            result = 0
            for i, a in enumerate(line):
                result += a * col_B[i]
            line_matrix.append(result)
        result_matrix.append(line_matrix)
    return result_matrix

#042 Inverser les mots d'une Chaine ?

def inverse(string):
    return " ".join([word[::-1] for word in string.split(" ")])

#043 Determinant Matrice 2 ?

def determinant_2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]

#044 Determinant Matrice 3 ?

def determinant_3(M):
    aei = M[0][0] * M[1][1] * M[2][2]
    bfg = M[0][1] * M[1][2] * M[2][0]
    cdh = M[0][2] * M[1][0] * M[2][1]
    ceg = M[0][2] * M[1][1] * M[2][0]
    bdi = M[0][1] * M[1][0] * M[2][2]
    afh = M[0][0] * M[1][2] * M[2][1]
    return aei + bfg + cdh - ceg - bdi - afh


# http://www.klubprepa.fr/Site/Document/ChargementExtrait.aspx?IdDocument=8817

#045

s = "Bonjour    tout    le   monde !"
s = " ".join(s.split())
print(s)

#046

def sum_dict(dictionnaire):
    return sum(dictionnaire.values())

#047

def elements_uniques(liste):
    if len(liste) == len(list(set(liste))):
        return True
    else:
        return False

#048

def pair(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
#049

def somme(liste):
    total = 0
    for nombre in liste:
        total += nombre
    return total

#050

#Remove : retire un élément spécifique de la liste
liste = ["a", "b", "c", "d", "e", "f"]
liste.remove("b")
print(liste)

#pop : retire un élément à un indice spécifique
liste = ["a", "b", "c", "d", "e", "f"]
liste.pop(2) #retire le c
print(liste)

#del : supprime un élément à un indice spécifique, mais ce n'est pas une méthode appartenant à la classe List.
liste = ["a", "b", "c", "d", "e", "f"]
del liste[3] #retire le d
print(liste)

# 051

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))

#052

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))

#053

n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)

#054 

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

#055

import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))

#056

lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)

#057

values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))

#058

import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

#059
class Person:
    name = "Person"  
    def __init__(self, name = None):
        self.name = name

jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))

#060

def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print(d)

printDict()

#061

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li)

printList()

#062

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)

#063

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14


#064

class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())

#065

def nbCheminsDist(dist):
    if dist == 0:
        return 1
 
    if dist < 0:
        return 0
 
    return nbCheminsDist(dist-1)+nbCheminsDist(dist-2)+nbCheminsDist(dist-3)


#066

class Chien:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def aboyer(self):
        print(f"Woof! Je m'appelle {self.nom}.")

#067

class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
    
    def informations(self):
        return f"Titre: {self.titre}, Auteur: {self.auteur}, Année: {self.annee}"


#068

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print(f(n))

#069

class Fraction :

    def __init__(self,a,b):
        self.num = a
        self.den = b

#070

class Employe:
    def __init__(self, nom, salaire_mensuel, augmentation):
        self.nom = nom
        self.salaire_mensuel = salaire_mensuel
        self.augmentation = augmentation
    
    def augmenter_salaire(self):
        augmentation_en_montant = self.salaire_mensuel * (self.augmentation / 100)
        self.salaire_mensuel += augmentation_en_montant

#071

class Banque:
    compteur_comptes = 0
    
    def __init__(self, titulaire, solde_initial):
        Banque.compteur_comptes += 1
        self.numero_compte = Banque.compteur_comptes
        self.titulaire = titulaire
        self.solde = solde_initial
    
    def deposer(self, montant):
        self.solde += montant
        print(f"Montant de {montant}€ déposé. Nouveau solde: {self.solde}€")
    
    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"Montant de {montant}€ retiré. Nouveau solde: {self.solde}€")
        else:
            print("Solde insuffisant.")

#072

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def perimetre(self):
        return 2 * (self.longueur + self.largeur)
    
    def aire(self):
        return self.longueur * self.largeur
    
    def est_carre(self):
        return self.longueur == self.largeur


#073

class Cours:
    def __init__(self, nom, enseignant, capacite):
        self.nom = nom
        self.enseignant = enseignant
        self.capacite = capacite
        self.etudiants_inscrits = []
    
    def ajouter_etudiant(self, etudiant):
        if len(self.etudiants_inscrits) < self.capacite:
            self.etudiants_inscrits.append(etudiant)
            print(f"{etudiant} a été inscrit au cours {self.nom}.")
        else:
            print(f"Le cours {self.nom} est complet.")
    
    def retirer_etudiant(self, etudiant):
        if etudiant in self.etudiants_inscrits:
            self.etudiants_inscrits.remove(etudiant)
            print(f"{etudiant} a été retiré du cours {self.nom}.")
        else:
            print(f"{etudiant} n'est pas inscrit au cours {self.nom}.")
    
    def afficher_etudiants(self):
        print(f"Étudiants inscrits au cours {self.nom}: {', '.join(self.etudiants_inscrits)}")


#074

class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True


#075

class Bibliotheque:
    def __init__(self):
        self.collection = []
    
    def ajouter_livre(self, livre):
        self.collection.append(livre)
    
    def emprunter_livre(self, titre):
        for livre in self.collection:
            if livre.titre == titre and livre.disponible:
                livre.disponible = False
                print(f"{livre.titre} a été emprunté.")
                return
        print(f"{titre} n'est pas disponible.")
    
    def retourner_livre(self, titre):
        for livre in self.collection:
            if livre.titre == titre and not livre.disponible:
                livre.disponible = True
                print(f"{livre.titre} a été retourné.")
                return
        print(f"{titre} ne peut pas être retourné.")


#076

class Vehicule:
    def __init__(self, modele, marque, annee):
        self.modele = modele
        self.marque = marque
        self.annee = annee
        self.vitesse = 0
    
    def accelerer(self, increment):
        self.vitesse += increment
        print(f"Le véhicule accélère de {increment} km/h. Vitesse actuelle: {self.vitesse} km/h.")
    
    def decelerer(self, decrement):
        self.vitesse -= decrement
        print(f"Le véhicule décélère de {decrement} km/h. Vitesse actuelle: {self.vitesse} km/h.")
    
    def afficher_vitesse(self):
        print(f"Vitesse actuelle du véhicule: {self.vitesse} km/h.")

#077

class CompteBancaire:
    def __init__(self, solde_initial):
        self.solde = solde_initial
    
    def deposer(self, montant):
        self.solde += montant
    
    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
        else:
            print("Fonds insuffisants.")
    
    def __str__(self):
        return f"Solde du compte: {self.solde} €"

#078

class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

class Catalogue:
    def __init__(self):
        self.produits = []
    
    def ajouter_produit(self, produit):
        self.produits.append(produit)
    
    def afficher_produits(self):
        for produit in self.produits:
            print(f"Produit: {produit.nom}, Prix: {produit.prix}€, Quantité: {produit.quantite}")
    
    def mettre_a_jour_stock(self, nom_produit, nouvelle_quantite):
        for produit in self.produits:
            if produit.nom == nom_produit:
                produit.quantite = nouvelle_quantite
                print(f"Quantité de {produit.nom} mise à jour: {produit.quantite}")

#079

import math

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def distance(self, autre_point):
        dx = self.x - autre_point.x
        dy = self.y - autre_point.y
        dz = self.z - autre_point.z
        return math.sqrt(dx**2 + dy**2 + dz**2)
    
    def translation(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz

#080

class Etudiant:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.notes = []
    
    def ajouter_note(self, note):
        self.notes.append(note)
    
    def moyenne_notes(self):
        if self.notes:
            return sum(self.notes) / len(self.notes)
        return 0
    
    def afficher_informations(self):
        print(f"Étudiant: {self.nom}, Âge: {self.age}")
        if self.notes:
            print("Notes:", ', '.join(map(str, self.notes)))
            print("Moyenne des notes:", self.moyenne_notes())
        else:
            print("Aucune note enregistrée.")

#081

class LivreEmpruntable(Produit):
    def __init__(self, nom, prix, quantite):
        super().__init__(nom, prix, quantite)
        self.emprunteur = None
    
    def emprunter(self, personne):
        if self.emprunteur is None:
            self.emprunteur = personne
            self.quantite -= 1
            print(f"{self.nom} a été emprunté par {personne}.")
        else:
            print(f"{self.nom} est déjà emprunté par {self.emprunteur}.")
    
    def retourner(self):
        if self.emprunteur:
            self.emprunteur = None
            self.quantite += 1
            print(f"{self.nom} a été retourné.")
        else:
            print(f"{self.nom} n'a pas été emprunté.")


#082

class Calculatrice:
    def __init__(self):
        self.memoire = 0
    
    def addition(self, nombre):
        self.memoire += nombre
    
    def soustraction(self, nombre):
        self.memoire -= nombre
    
    def multiplication(self, nombre):
        self.memoire *= nombre
    
    def division(self, nombre):
        if nombre != 0:
            self.memoire /= nombre
        else:
            print("Division par zéro.")
    
    def effacer_memoire(self):
        self.memoire = 0

#083

class Voyage:
    def __init__(self, destination, cout_total):
        self.destination = destination
        self.cout_total = cout_total
        self.participants = []
    
    def ajouter_participant(self, participant):
        self.participants.append(participant)
    
    def calculer_participation(self):
        if self.participants:
            part_individuelle = self.cout_total / len(self.participants)
            return part_individuelle
        return 0
    
    def afficher_informations(self):
        print(f"Voyage à {self.destination}")
        print("Coût total:", self.cout_total)
        for participant in self.participants:
            print(f"- {participant}")
        print("Participation individuelle:", self.calculer_participation())

#084

import math

class Forme:
    def calculer_aire(self):
        pass
    
    def calculer_perimetre(self):
        pass

#085

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    
    def calculer_aire(self):
        return math.pi * self.rayon**2
    
    def calculer_perimetre(self):
        return 2 * math.pi * self.rayon

#086

class ChaineCaracteres:
    def __init__(self, chaine):
        self.chaine = chaine
    
    def inverser(self):
        return self.chaine[::-1]
    
    def compter_caracteres(self):
        return len(self.chaine)
    
    def est_palindrome(self):
        return self.chaine == self.chaine[::-1]


#087

class Evenement:
    def __init__(self, nom, date, heure):
        self.nom = nom
        self.date = date
        self.heure = heure

class Agenda:
    def __init__(self):
        self.evenements = []
    
    def ajouter_evenement(self, evenement):
        self.evenements.append(evenement)
    
    def afficher_evenements(self):
        for evenement in self.evenements:
            print(f"{evenement.nom} - {evenement.date} à {evenement.heure}")
    
    def afficher_evenements_date(self, date):
        for evenement in self.evenements:
            if evenement.date == date:
                print(f"{evenement.nom} à {evenement.heure}")


#088

class Bouteille:
    def __init__(self, nom, contenance):
        self.nom = nom
        self.contenance = contenance
        self.niveau = 0
    
    def verser(self, volume):
        if volume <= self.niveau:
            self.niveau -= volume
        else:
            print("Niveau insuffisant.")
    
    def remplir(self):
        self.niveau = self.contenance
    
    def afficher_niveau(self):
        print(f"Niveau de {self.nom}: {self.niveau} ml")


#089

import random

class JeuDeCartes:
    def __init__(self):
        symboles = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        self.cartes = [f"{valeur} de {symbole}" for symbole in symboles for valeur in valeurs]
    
    def melanger(self):
        random.shuffle(self.cartes)
    
    def piocher(self):
        if self.cartes:
            return self.cartes.pop()
        return "Aucune carte restante."
    
    def nombre_cartes_restantes(self):
        return len(self.cartes)

#090

class PostIt:
    def __init__(self, titre, contenu, couleur):
        self.titre = titre
        self.contenu = contenu
        self.couleur = couleur
    
    def afficher(self):
        print(f"--- {self.titre} ---")
        print(self.contenu)
        print(f"Couleur: {self.couleur}")

    def changer_couleur(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur


#091

import datetime

class ReservationHotel:
    def __init__(self, nom, arrivee, depart, personnes, tarif_journalier):
        self.nom = nom
        self.arrivee = arrivee
        self.depart = depart
        self.personnes = personnes
        self.tarif_journalier = tarif_journalier
    
    def afficher_details(self):
        print(f"Réservation pour {self.personnes} personnes:")
        print(f"Nom: {self.nom}")
        print(f"Arrivée: {self.arrivee.strftime('%d/%m/%Y')}")
        print(f"Départ: {self.depart.strftime('%d/%m/%Y')}")
    
    def calculer_cout_total(self):
        duree_sejour = (self.depart - self.arrivee).days
        cout_total = duree_sejour * self.tarif_journalier
        return cout_total

#092

class Animal:
    def __init__(self, nom, espece, age):
        self.nom = nom
        self.espece = espece
        self.age = age

class Zoo:
    def __init__(self):
        self.animaux = []
    
    def ajouter_animal(self, animal):
        self.animaux.append(animal)
    
    def afficher_animaux(self):
        for animal in self.animaux:
            print(f"{animal.nom} - {animal.espece} ({animal.age} ans)")
    
    def afficher_animaux_espece(self, espece):
        for animal in self.animaux:
            if animal.espece == espece:
                print(f"{animal.nom} - {animal.espece} ({animal.age} ans)")

#093

class Article:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

class Facture:
    def __init__(self):
        self.articles = []
    
    def ajouter_article(self, article):
        self.articles.append(article)
    
    def calculer_montant_total(self):
        montant_total = sum(article.prix * article.quantite for article in self.articles)
        return montant_total
    
    def afficher_facture(self):
        for article in self.articles:
            total_article = article.prix * article.quantite
            print(f"{article.nom} - {article.quantite} x {article.prix} € = {total_article} €")
        montant_total = self.calculer_montant_total()
        print(f"Montant total: {montant_total} €")

#094

class CompteEpargne:
    def __init__(self, solde_initial, taux_interet):
        self.solde = solde_initial
        self.taux_interet = taux_interet
    
    def deposer(self, montant):
        self.solde += montant
    
    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
        else:
            print("Fonds insuffisants.")
    
    def calculer_interet(self, mois):
        interet = (self.solde * self.taux_interet / 100) * mois / 12
        return interet

#095

class Propriete:
    def __init__(self, adresse, prix, description):
        self.adresse = adresse
        self.prix = prix
        self.description = description

class AgenceImmobilier:
    def __init__(self):
        self.proprietes = []
    
    def ajouter_propriete(self, propriete):
        self.proprietes.append(propriete)
    
    def afficher_proprietes(self):
        for propriete in self.proprietes:
            print(f"{propriete.adresse} - {propriete.prix} €")
    
    def rechercher_par_prix_max(self, prix_max):
        resultats = []
        for propriete in self.proprietes:
            if propriete.prix <= prix_max:
                resultats.append(propriete)
        return resultats
#096

def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    milieu = len(liste) // 2
    gauche = tri_fusion(liste[:milieu])
    droite = tri_fusion(liste[milieu:])
    return fusionner(gauche, droite)

def fusionner(gauche, droite):
    resultat = []
    i, j = 0, 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat

#097

def est_premier(nombre):
    if nombre <= 1:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True

def liste_nombres_premiers(n):
    nombres_premiers = []
    for i in range(2, n):
        if est_premier(i):
            nombres_premiers.append(i)
    return nombres_premiers

#098

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a


#099

def facteurs_premiers(nombre):
    facteurs = []
    diviseur = 2
    while diviseur <= nombre:
        if nombre % diviseur == 0:
            facteurs.append(diviseur)
            nombre //= diviseur
        else:
            diviseur += 1
    return facteurs


#100

def somme_chiffres(nombre):
    somme = 0
    while nombre > 0:
        somme += nombre % 10
        nombre //= 10
    return somme


#101

def nombre_plus_frequent(liste):
    compteurs = {}
    for nombre in liste:
        if nombre in compteurs:
            compteurs[nombre] += 1
        else:
            compteurs[nombre] = 1
    nombre_plus_frequent = max(compteurs, key=compteurs.get)
    return nombre_plus_frequent

#102

def produit_scalaire(vecteur1, vecteur2):
    if len(vecteur1) != len(vecteur2):
        return None
    produit = sum(x * y for x, y in zip(vecteur1, vecteur2))
    return produit

#103

def est_palindrome_phrase(phrase):
    phrase = phrase.replace(" ", "").lower()
    return phrase == phrase[::-1]

#104

def table_multiplication(nombre, multiplicateur):
    for i in range(1, multiplicateur + 1):
        produit = nombre * i
        print(f"{nombre} x {i} = {produit}")


#105

def tri_bulles(liste):
    n = len(liste)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]


#106

def decimal_vers_binaire(nombre):
    binaire = ''
    while nombre > 0:
        reste = nombre % 2
        binaire = str(reste) + binaire
        nombre //= 2
    return binaire


#107

def compter_voyelles(chaine):
    voyelles = "aeiouAEIOU"
    compteur = 0
    for caractere in chaine:
        if caractere in voyelles:
            compteur += 1
    return compteur

#108

def tri_insertion(liste):
    for i in range(1, len(liste)):
        element = liste[i]
        j = i - 1
        while j >= 0 and element < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = element


#109

def sous_liste_maximale(liste):
    max_global = max_local = liste[0]
    for nombre in liste[1:]:
        max_local = max(nombre, max_local + nombre)
        max_global = max(max_global, max_local)
    return max_global

#110

def tri_rapide(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[len(liste) // 2]
    gauche = [x for x in liste if x < pivot]
    milieu = [x for x in liste if x == pivot]
    droite = [x for x in liste if x > pivot]
    return tri_rapide(gauche) + milieu + tri_rapide(droite)


#111

def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    
    milieu = len(liste) // 2
    gauche = liste[:milieu]
    droite = liste[milieu:]
    
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    
    return fusionner(gauche, droite)

#112

def fusionner(gauche, droite):
    resultat = []
    i = j = 0
    
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    
    return resultat

#113

def sous_sequence_maximale(liste):
    max_global = max_local = liste[0]
    for nombre in liste[1:]:
        max_local = max(nombre, max_local + nombre)
        max_global = max(max_global, max_local)
    return max_global


#114
   
def est_palindrome(chaine):
    chaine = chaine.lower().replace(" ", "")
    return chaine == chaine[::-1]


#115

def plus_grand_nombre(liste):
    return max(liste)


#116

def tri_a_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]


#117

def combinaisons(n, k):
    if k == 0 or k == n:
        return 1
    return combinaisons(n - 1, k - 1) + combinaisons(n - 1, k)


#118

def permutations(n, k):
    if k == 0:
        return 1
    return n * permutations(n - 1, k - 1)


#119

def pgcd_multiple(nombres):
    def pgcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    result = nombres[0]
    for i in range(1, len(nombres)):
        result = pgcd(result, nombres[i])
    return result


#120

def sous_liste_maximale(liste):
    max_global = max_local = liste[0]
    for nombre in liste[1:]:
        max_local = max(nombre, max_local + nombre)
        max_global = max(max_global, max_local)
    return max_global


#121

def fusion_compte_inversions(gauche, droite):
    i = j = inversions = 0
    resultat = []
    
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
            inversions += len(gauche) - i
    
    resultat += gauche[i:]
    resultat += droite[j:]
    
    return resultat, inversions

#122

def tri_compte_inversions(liste):
    if len(liste) <= 1:
        return liste, 0
    
    milieu = len(liste) // 2
    gauche, inversions_gauche = tri_compte_inversions(liste[:milieu])
    droite, inversions_droite = tri_compte_inversions(liste[milieu:])
    fusionnee, inversions_fusion = fusion_compte_inversions(gauche, droite)
    
    inversions_total = inversions_gauche + inversions_droite + inversions_fusion
    return fusionnee, inversions_total


#123

def nombre_voyelles(chaine):
    voyelles = "aeiouAEIOU"
    compteur = 0
    for char in chaine:
        if char in voyelles:
            compteur += 1
    return compteur


#124

def somme_chiffres(nombre):
    somme = 0
    while nombre > 0:
        somme += nombre % 10
        nombre //= 10
    return somme


#125

def est_carre_magique(matrice):
    n = len(matrice)
    somme_diagonale1 = sum(matrice[i][i] for i in range(n))
    somme_diagonale2 = sum(matrice[i][n - 1 - i] for i in range(n))
    if somme_diagonale1 != somme_diagonale2:
        return False
    
    for i in range(n):
        somme_ligne = sum(matrice[i])
        somme_colonne = sum(matrice[j][i] for j in range(n))
        if somme_ligne != somme_diagonale1 or somme_colonne != somme_diagonale1:
            return False
    
    return True


#126



#127



#128



#129



#130




