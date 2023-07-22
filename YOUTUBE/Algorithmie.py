# https://www.youtube.com/watch?v=iNeqb-URBj4&ab_channel=Foxxpy-Mathématiquesetalgorithmie

# 001 Nombre premier ?
    
def is_prime(n):
    for d in range(2,n):
        if n % d == 0:
            return False
    return True

# 002 Liste des Nombres premiers dans un intervalle ?

def get_primes_list(inf, sup):
    primes_list = []
    for nbr in range(inf, sup+1):
        if is_prime(nbr):
            primes_list.append(nbr)
    return primes_list

print(get_primes_list(1, 100))



