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

