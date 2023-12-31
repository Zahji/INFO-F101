# https://www.youtube.com/watch?v=Dz-Izb1bUio&list=PL6JtJ0Q7T-YxUzIjSzUSXe18yWZ2jXtGz&index=1&ab_channel=Foxxpy-Mathématiquesetalgorithmie

#1
def recursion_multiplication(n1, n2, i=1):
    if i < n2 :
        n1 = recursion_multiplication(n1, n2, i = i+1) + n1
    return n1

n1 = 3
n2 = 5
resultat = recursion_multiplication(n1, n2)
print("Récursion: " + str(resultat))
print("Multiplication: " + str(n1*n2))

#2
def recursion_factorielle(n):
    if n > 2:
        n *= recursion_factorielle(n-1)
    return n

#3
def recursion_inversion_string(s):
    new_s = s[-1]
    if len(s) > 1:
        new_s += recursion_inversion_string(s[0:-1])
    return new_s