# Anciens examens INFO-F101

# ---------- 2012_2013 ---------- #

# ---------- QUESTION 1 --------- #


# ---------- 1) Programmation Impérative -----------

somme = 0
for nombre in range(1, 6):
    somme = somme + nombre
print("Somme (Impératif) :", somme)


# --------- 2) Programmation Fonctionnelle --------- 

def doubler_nombres(liste):
    resultat = []
    for nombre in liste:
        resultat.append(nombre * 2)
    return resultat

ma_liste = [1, 2, 3, 4, 5]
resultat_magique = doubler_nombres(ma_liste)

print("Résultat magique :", resultat_magique)

# --------- 3) Programmation Orienté Objet --------- 

class SuperHero:
    def __init__(self, nom, pouvoir):
        self.nom = nom
        self.pouvoir = pouvoir

    def utiliser_pouvoir(self):
        print(self.nom, "utilise son pouvoir", self.pouvoir)

superman = SuperHero("Superman", "voler")
superman.utiliser_pouvoir()

# ---------- QUESTION 2 --------- #

def foo(x):
    return x*x

def resultat_foo(x):
    while True:
        try:
            x = float(input("Entrez une valeur pour x : "))
            resultat = foo(x)
            print("Le résultat de foo(x) est :", resultat)
            break 
        except KeyboardInterrupt:
            print
    