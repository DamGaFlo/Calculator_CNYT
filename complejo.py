import math


ERROR = 0.000000001


class Complejo():
    def __init__(self,real,complejo,polar = False):
        self.real = real
        self.complejo = complejo
        #representacion carteciana o polar (True si es cartesiana)
        self.isPolar = polar

    def __eq__(self,complejo):
        return self.real == complejo.real and self.complejo == complejo.complejo

    def getReal(self):
        return self.real

    def getComplejo(self):
        return self.complejo

    def realIs0(self):
        if (self.real<=ERROR and self.real>=-ERROR):
            return True
        return False
    
    def complejoIs0(self):
        if (self.complejo<=ERROR and self.complejo>=-ERROR):
            return True
        return False

    def is0(self):
        if self.realIs0() and self.complejoIs0():
            return True
        return False
    
    def __add__(self,value):
        return Complejo(self.real+value.real,value.complejo+self.complejo)

    def __sub__(self,value):
        return Complejo(self.real-value.real,value.complejo-self.complejo)

    def __mul__(self,value):
        if(type(value)==int):
            return value*self;
        return Complejo(value.real*self.real-value.complejo*self.complejo,self.real*value.complejo+self.complejo*value.real)

    def divInt(self,value):
        return Complejo(self.getReal()/value,self.getComplejo()/value)

    def __truediv__(self,value):
        if value.is0():
            raise TypeError("No se puede dividir por cero")
        elif self.is0():
            return Complejo(0,0)
        conjugado = (value*value.conj()).getReal()
        numerador = self*value.conj()

        return numerador.divInt(conjugado)
    def __neg__(self):
        return Complejo(-self.real,-self.complejo)
    def __rmul__(self,value):
        n = Complejo(value,0)
        return n*self;
        
    
    def modulo(self):
        return (self.real**2+self.complejo**2)**(1/2)

    def fase(self):
        return math.atan2(self.complejo,self.real)
        
    
    def conj(self):
        return Complejo(self.real,-self.complejo)
    
    def __str__(self):
        return str(self.real)+" "+str(self.complejo)+"i"
    """Conversión entre representaciones polar y cartesiano"""
    
    def toPolar(self):
        return (self.modulo(),self.fase())

    

