# https://www.youtube.com/watch?v=iNeqb-URBj4&ab_channel=Foxxpy-Mathématiquesetalgorithmie

# 001 Nombre premier ?
    
def is_prime(n):
    for d in range(2,n):
        if n % d == 0:
            return False
    return True

# 002 Liste des Nombres premiers dans un intervalle ?

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

print(get_primes_list(1, 100))

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

#004

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

print(get_perfects_list(1, 100))
