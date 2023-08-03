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

#066

#067

#068

#069

#070

#071

#072

#073

#074

#075

#076

#077
