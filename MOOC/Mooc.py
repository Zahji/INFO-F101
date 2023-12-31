#------------------------------ MOOC PARTIE 3 -----------------------------#
#------------------------------- Exercice 1 -------------------------------#

a = int(input())
b = int(input())
c = int(input())
if a == b :
    print(a)
elif a == c :
    print (a)
elif b == c :
    print(b)

#------------------------------- Exercice 2 -------------------------------#

temperature = int(input())
if temperature <= 10 and temperature > 0:
    print("Il va faire frais.")
elif temperature <= 0:
    print("Il va faire froid.")

#------------------------------- Exercice 3 -------------------------------#

a = int(input())
b = int(input())
c = int(input())

if c == 1:
    print(a + b)
elif c == 2:
    print(a - b)
elif c == 3:
    print(a * b)
elif c == 4:
    print(a ** 2 + a * b)
else:
    print("Erreur")

#------------------------------- Exercice 4 -------------------------------#

a = int(input())
if a % 2==0:
    print("True")
else:
    print("False")

#------------------------------- Exercice 5 -------------------------------#

a = int(input())
b = int(input())
if a % b == 0 or b % a == 0:
    print("False")
else:
    print("True")

#------------------------------- Exercice 6 -------------------------------#

a = float(input())
b = float(input())
if a >= 0 and b >= 0 :
    print((a*b)**(1/2))
else : 
    print("Erreur")

#------------------------------- Exercice 7 -------------------------------#

mise = int(input()) # pari (0 et 16)
x = int(input()) # tirage (0 et 12)

if mise == 13 and x%2 == 0 \
or mise == 14 and x%2 == 1 \
or mise == 15 and ((x%2 == 1 and x != 11) or x==12 )\
or mise == 16 and ((x%2 == 0 and x != 12 and x != 0) or x == 11 ):  
    print(20)
elif mise == x:
    print(120)
else :
    print(0)

#------------------------------- Exercice 8 -------------------------------#
    
import math as m

lettre = str(input())
arete = float(input())

if lettre == "T":
    volume = m.sqrt(2) * arete ** 3 / 12
elif lettre == "C":
    volume = arete ** 3
elif lettre == "O":
    volume = m.sqrt(2) * arete ** 3 / 3
elif lettre == "D":
    volume = (15 + 7 * m.sqrt(5)) * arete ** 3 / 4
elif lettre == "I":
    volume = 5 * (3 + m.sqrt(5)) * arete ** 3 / 12
else:
    volume = "Polyèdre non connu"

print(volume)

#------------------------------- Exercice 9 -------------------------------#

x = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
while x != 42:
    print("Mauvaise réponse.")
    x = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
print("Bravo !")

#------------------------------- Exercice 10 ------------------------------#

entree = int(input())
compagnie = 0
employee = 0

while entree != -1:
    employee += entree
    compagnie += 1
    entree = int(input())

print(employee / compagnie)

#------------------------------- Exercice 11 ------------------------------#

taille = int(input())
for i in range(taille):
    print("X" * taille)

#------------------------------- Exercice 12 ------------------------------#

taille = int(input())
for i in range(taille):
    print((i) * " " + "X" * (taille - i))

#------------------------------- Exercice 13 ------------------------------#

a = int(input())
b = 0
if a >= 0:
    for i in range(a):
        b += int(input())
else:
    a = 0
    while a != "F":
        b += int(a)
        a = input()
print(b)

#------------------------------- Exercice 14 ------------------------------#

import random
secret = random.randint(0, 100)
essais = 6
essaisActuel = 0

while essaisActuel != essais:
    essaisActuel += 1
    proposition = int(input())
    if proposition == secret:
        print("Gagné en", essaisActuel, "essai(s) !")
        essaisActuel = essais
    elif essaisActuel == essais:
        print("Perdu ! Le secret était", secret)
    elif proposition > secret:
        print("Trop grand")
    elif proposition < secret:
        print("Trop petit")

#------------------------------- Exercice 15 ------------------------------#

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j, end = " ")
    print()

#------------------------------ MOOC PARTIE 4 -----------------------------#
#------------------------------- Exercice 1 -------------------------------#

def deux_egaux(a, b, c):
    return  a == b or a == c or b == c
x = int(input())
y = int(input())
z = int(input())
print(deux_egaux(x, y, z))

#------------------------------- Exercice 2 -------------------------------#

def soleil_leve(a, b, c):
    if b == 12 and a == 12:
        return False
    elif b == 0 and a == 0:
        return True
    elif a > b :
        if a > c >= b :
            return False
        else:
            return True
    elif a <= c < b :
        return True
    return False

#------------------------------- Exercice 3 -------------------------------#

def premier(x):
    a=1
    b=1
    while a >=x and x % a !=0:
        b+=1
        a+=1
    if x == 1:
        return False
    if not(x %2==0 or x % 3 == 0 or x%5==0 or x%7==0 and x%b == 0):
        res = True
    elif x ==2 or x ==3 or x==5 or x==7:
        res =True
    elif x%b == 0:
        res = False
    else :
        res = False
    return res
z = int(input())
p=0
while p < z:
    if premier (p) == True and p!=1:
        print(p)
    p +=1 

#------------------------------- Exercice 4 --------------------------------#

import random
def alea_dice(x):
    random.seed(x)
    res = True
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    if min(a,b,c) == 1 and max(a,b,c) == 4 and (a == 2 or b == 2 or c == 2):
        return res
    else : 
        return False

#------------------------------- Exercice 5 --------------------------------#

def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    diff = (x20 * 20 + x10 * 10 + x5 * 5 +x2 * 2 + x1 * 1) - prix
    if diff < 0 :
        res = (None, None, None, None, None)
    else:
        x20, diff = divmod(diff, 20)
        x10, diff = divmod(diff, 10)
        x5, diff = divmod(diff, 5)
        x2, diff = divmod(diff, 2)
        x1, diff = divmod(diff, 1)
        res = (x20, x10, x5, x2, x1)
    return res

#resultat = rendre_monnaie(45, 1, 1, 1, 1, 1)
#print(resultat)

#------------------------------- Exercice 6 --------------------------------#

def somme(a = 0, b = 1):
    return a + b

#resultat = somme(24, 18)
#print(resultat)

#------------------------------- Exercice 7 --------------------------------#

from math import sqrt
def rac_eq_2nd_deg(a, b, c):
    delta = (b**2) - 4*a*c

    if delta < 0:
        x = tuple()
    elif delta == 0:
        x = (-b / (2*a))
    else:
        x1, x2 = ((-b- sqrt(delta)) / (2*a)), ((-b+ sqrt(delta)) / (2*a))
        x = (x1, x2)
    return x

resultat = rac_eq_2nd_deg(1.0, 1.0,-2.0)
print(resultat)

#------------------------------- Exercice 8 --------------------------------#

def catalan(n):
    a=1
    b=1
    c=1
    if n>=0:
        for i in range(1,n+1):
            a=a*i
        for i in range(1,2*n+1):
            b=b*i
        for i in range(1,n+2):
            c=c*i
    d=(b)//(c*a)
    return d

#------------------------------- Exercice 9 --------------------------------#

def bat(joueur_1,joueur_2):
    res=True
    if (joueur_1==0 and joueur_2==2) or (joueur_1==2 and joueur_2==1) or (joueur_1==1 and joueur_2==0):
        return res
    else:
        return False

 
#------------------------------ MOOC PARTIE 5 -----------------------------#   
#------------------------------- Exercice 1 -------------------------------#

def transcription_clavier(texte):
    return texte.replace('%','M')

#------------------------------- Exercice 2 -------------------------------#

def plus_grand_bord(mot):
    i = 0
    while mot[i:] != mot[:-i]:
        i += 1
    return mot[i:]

#------------------------------- Exercice 3 -------------------------------#

def premier(n) :
    r = (n-1)
    bo = True
    for r in range(r,1,-1) :
        a = n%r
        if a == 0 :
            bo = False
    if n==1 or n==0 :
        bo = False
    return(bo)
def prime_numbers(nb) :
    i = 0
    e = 2
    c = []
    if  type(nb) != int or nb < 0:
        c = None
    else :
        while i < nb :
            f = premier(e)
            if f :
                c.append(e)
                i+=1
            e+=1
    return c

#------------------------------- Exercice 4 -------------------------------#

def anagrammes(v, w):
    return sorted(v) == sorted(w)

#------------------------------- Exercice 5 -------------------------------#

def dupliques(v):
    res=False
    for lettre in v:
        if v.count(lettre)>=2:
            res = True
    return res

#------------------------------- Exercice 6 -------------------------------#

def my_insert(a,b):
    x=[]
    if type(b) is int :
        for i in a:
            x.append(i)
        x.append(b)
        x=sorted(x)
    else:
        x=None
    return(x)

#------------------------------- Exercice 7 -------------------------------#

def my_pow(m, b):
    if type(b) == float and type(m) == int:
        list_pow = []
        for i in range(m):
            list_pow.append(b ** i)
    else:
        list_pow = None

    return list_pow
print(my_pow(8, 2.4))

#------------------------------- Exercice 8 -------------------------------#

def decompresse(lst):
    t = [element[1] for element in lst for repetition in range(element[0])]
    return t
print(decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]))

#------------------------------- Exercice 9 -------------------------------#

def init_mat(m, n):
    return [[0 for j in range(n)] for i in range(m)]
print(init_mat(2,3))

#------------------------------- Exercice 10 -------------------------------#

def print_mat(M) :
    if M!=[] :
        for i in M:
            for j in i :
                print(j,end =" ")
            print(end="\n")
    else:
        print("")
ma_matrice = eval(input())
print_mat(ma_matrice)

def trace(M) :
    x=0
    n=0
    for i in M:
        x = x + i[n]
        n=n+1
    return x

#------------------------------- Exercice 11 -------------------------------#

def trace(M):
    sum = 0 
    n = len(M) 
    for i in range(n):
        sum += M[i][i] 
    return sum

#------------------------------ MOOC PARTIE 6 -----------------------------#   
#------------------------------- Exercice 1 -------------------------------#

def inventaire(x,y):
    d=set()
    for i in y:
        d.add(x[i])
    return d

#------------------------------- Exercice 2 -------------------------------#

def calcul_prix(produits, catalogue):
    prix_total = 0
    for e in produits: 
        prix_total += produits[e] * catalogue[e]
    return prix_total

#------------------------------- Exercice 3 -------------------------------#

from math import *
def bonne_planete(diametre):
    if pi*(diametre)**2 >= 50*1000:
        res=True
    else :
        res=False
    return res
k = float(input())
if bonne_planete(k):
    print("Bonne planète")
else:
    print("Trop petite")

#------------------------------- Exercice 4 -------------------------------#

def check_rows(grid):
    n=1
    for i in grid:
        for j in range(len(i)):
            if i[j] in i[j+1:]:
                n=0
    if n == 1 :
        return True
    else:
        return False


