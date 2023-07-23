# https://www.youtube.com/watch?v=iNeqb-URBj4&ab_channel=Foxxpy-Mathématiquesetalgorithmie

# 001 Nombre premier ?
    
def is_prime(n):
    for d in range(2,n):
        if n % d == 0:
            return False
    return True

# 002 Nombres premiers dans un intervalle ?

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

# 003 Nombre Parfait ?

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

#008 Conversion Temps

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