"""
Autor Jordi Maylinch

El programa et demana un nombre enter i et mostra per pantalla els primers nombres primers
"""


import sys

class llista_primers:

    """
    Calcula els "n" primers nombres primers

    >>> llista_primers(5).llista
    [2, 3, 5, 7, 11]
    >>> llista_primers(0).llista
    [2]
    >>> llista_primers(1).llista
    [2]
    """

    def __init__(self, n):
        """
        La variable "llista" tindra tants numeros com entrem per terminal
        """
        self.n = n
        self.llista = []
        self.busca()

    def busca(self):
        """
        Busca recursivament els nombres primers fins a n
        """

        #Si la llista esta buida afegeix el nombre '2'
        if (len(self.llista) == 0):
            self.llista.append(2)
            self.busca()

        #Si no esta buida busca un nombre primer a partir de l'ultim trobat fins arribar a n
        elif (len(self.llista) < self.n):
            trobat = False
            seguent = self.llista[-1]+1
            while not trobat:
                for i in self.llista:
                    if seguent%i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else:
                        trobat = True
            self.llista.append(seguent)
            self.busca()

##si es el document principal executa aquest codi
if __name__ == '__main__':
    """
    El valor que donem, per defecte sera un String. En el main es passa a int, i d'aquesta manera, el codi el pot utilitzar.
    Mostra per pantalla el resultat
    """
    l = llista_primers(int(sys.argv[1]))
    print l.llista
