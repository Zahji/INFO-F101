# Les Exercices suivant sont d'un niveau plus avancés :

# Premier Lien : 

# Exos 1 :

def nbCheminsDist(dist):
    if dist == 0:
        return 1
 
    if dist < 0:
        return 0
 
    return nbCheminsDist(dist-1)+nbCheminsDist(dist-2)+nbCheminsDist(dist-3)