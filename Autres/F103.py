# Cours d'Algorithmie F103 

class Complexe:
    def __init__(self, re=0., im=0.):
        self.__re = re
        self.__im = im

    def re(self):
        return self.__re
    @property
    def im(self):
        return self.__im
    def __str__(self):
        return f"{self.re:g} + {self.im:g}i"
    def __iadd__(self, z):
        if isinstance(z, (int, float)): 
            z = Complexe(re=z, im=0)