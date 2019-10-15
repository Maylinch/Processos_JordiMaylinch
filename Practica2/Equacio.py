class Equacio:
    def __init__(self,eq):
        self.eq = eq

    def calcula(self):
        self.a, self.b , self.c, self.d, self.e = self.eq.split(" ")
        if self.a[0] == "x":
            self.a = 1
        else:
            self.a=self.a[0:len(self.a)-1]

        if self.b == "+":
            self.r= float(self.e) - float(self.c)
        else:
            self.r= float(self.e) + float(self.c)

        self.r = float(self.r) / float(self.a)

        print float(self.r)
