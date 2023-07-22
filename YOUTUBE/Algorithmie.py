# https://www.youtube.com/watch?v=iNeqb-URBj4&ab_channel=Foxxpy-Mathématiquesetalgorithmie

# 001 Nombre premier ?
    
def is_prime(n):
    for d in range(2,n):
        if n % d == 0:
            return False
    return True




