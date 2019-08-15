import math
import unittest


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
    
    def suma(self,value):
        return Complejo(self.real+value.real,value.complejo+self.complejo)

    def resta(self,value):
        return Complejo(self.real-value.real,value.complejo-self.complejo)

    def mult(self,value):
        return Complejo(value.real*self.real-value.complejo*self.complejo,self.real*value.complejo+self.complejo*value.real)

    def divInt(self,value):
        return Complejo(self.getReal()/value,self.getComplejo()/value)

    def div(self,value):
        if value.is0():
            raise TypeError("No se puede dividir por cero")
        elif self.is0():
            return Complejo(0,0)
        conjugado = value.mult(value.conj()).getReal()
        numerador = self.mult(value.conj())

        return numerador.divInt(conjugado)
    
    def modulo(self):
        return (self.real**2+self.complejo**2)**(1/2)

    def fase(self):
        return math.atan2(self.complejo,self.real)
        
    
    def conj(self):
        return Complejo(self.real,-self.complejo)
    
    def getStr(self):
        return str(self.real)+" "+str(self.complejo)
    """Conversión entre representaciones polar y cartesiano"""
    
    def toPolar(self):
        return (self.modulo(),self.fase())

    


class Test(unittest.TestCase):
    
    def test_deberiaSumar(self):
        a = Complejo(3,2)
        b = Complejo(7,2)
        self.assertEqual(Complejo(10,4),a.suma(b))

        
    def test_deberiaRestar(self):
        a = Complejo(3,2)
        b = Complejo(7,2)
        self.assertEqual(Complejo(-4,0),a.resta(b))

        
    def test_deberiaMultiplicar(self):
        a = Complejo(5,2)
        b = Complejo(3,-4)
        self.assertEqual(Complejo(23,-14),a.mult(b))

        a = Complejo(17,-5)
        b = Complejo(0,0)
        self.assertEqual(Complejo(0,0),a.mult(b))

    def test_deberiaDividir(self):
        a = Complejo(5,2)
        b = Complejo(3,-4)
        self.assertEqual(Complejo(7/25,26/25),a.div(b))

    def test_noDeberiaDividir(self):
        a = Complejo(5,2)
        b = Complejo(0,0)
        try:
            a.div(b)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_deberiaConjugar(self):
        
        a = Complejo(5,2)
        self.assertEqual(Complejo(5,-2),a.conj())

        a = Complejo(0,17)
        self.assertEqual(Complejo(0,-17),a.conj())

    

        
        
    
def main():
    c=Complejo(-3,-3)
    n=Complejo(-3,-3)
    print(c==n)
    print(c.toPolar())
    print(c.getStr())
    print(c.modulo())
    print(math.degrees(c.fase()))
    
if __name__ == '__main__':
    unittest.main() 
    #main()
    
