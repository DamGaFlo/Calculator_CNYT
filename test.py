from complejo import Complejo
import unittest




class Test(unittest.TestCase):
    
    def test_deberiaSumar(self):
        a = Complejo(3,2)
        b = Complejo(7,2)
        self.assertEqual(Complejo(10,4),a+b)

        
    def test_deberiaRestar(self):
        a = Complejo(3,2)
        b = Complejo(7,2)
        self.assertEqual(Complejo(-4,0),a-b)

        
    def test_deberiaMultiplicar(self):
        a = Complejo(5,2)
        b = Complejo(3,-4)
        self.assertEqual(Complejo(23,-14),a*b)

        a = Complejo(17,-5)
        b = Complejo(0,0)
        self.assertEqual(Complejo(0,0),a*b)

    def test_deberiaDividir(self):
        a = Complejo(5,2)
        b = Complejo(3,-4)
        self.assertEqual(Complejo(7/25,26/25),a/b)

    def test_noDeberiaDividir(self):
        a = Complejo(5,2)
        b = Complejo(0,0)
        try:
            a/b
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_deberiaConjugar(self):
        
        a = Complejo(5,2)
        self.assertEqual(Complejo(5,-2),a.conj())

        a = Complejo(0,17)
        self.assertEqual(Complejo(0,-17),a.conj())
        


unittest.main()
    
