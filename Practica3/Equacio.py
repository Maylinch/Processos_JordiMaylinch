class Equacio:
    def __init__(self,eq):
        self.eq = eq

    def calcula(self):
        try:
            self.a, self.b , self.c, self.d, self.e = self.eq.split(" ")
            if self.a[0] == "x":
                self.a = 1
            else:
                self.a=self.a[0:len(self.a)-1]

        except:
            return ("l'equacio no segueix el format Ax + B = C")

        try:
            self.a= float(self.a)
            self.c= float(self.c)
            self.e= float(self.e)

        except:
            return ("l'equacio conte caracter no calculables: "+self.eq)

        try:
            if self.b == "+":
                self.r= float(self.e) - float(self.c)
            elif self.b == "-":
                self.r= float(self.e) + float(self.c)

            self.r = float(self.r) / float(self.a)

            return float(self.r)
        except:
            return ("Operador no valid: "+self.b)
