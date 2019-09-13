from complejo import Complejo
from complexMatrix import ComplexMatrix
import unittest


class Test(unittest.TestCase):

    def test_deberia_sumar(self):
        a = ComplexMatrix.toComplexM([[(1,2),(4,5)],[(-5,4),(1,1)],[(1,3),(3,7)]])
        b = ComplexMatrix.toComplexM([[(3,2),(1,2)],[(-1,1),(3,3)],[(2,1),(-2,-2)]])
        c = ComplexMatrix.toComplexM([[(4,4),(5,7)],[(-6,5),(4,4)],[(3,4),(1,5)]])

        a = ComplexMatrix(a)
        b = ComplexMatrix(b)
        c = ComplexMatrix(c)

        self.assertEqual(a+b,c)
    def test_no_deberia_sumar(self):
        a = ComplexMatrix.toComplexM([[(1,2),(4,5)],[(-5,4),(1,1)],[(1,3),(3,7)]])
        b = ComplexMatrix.toComplexM([[(3,2),(1,2)],[(-1,1),(3,3)]])
        c = ComplexMatrix.toComplexM([[(4,4),(5,7)],[(-6,5),(4,4)],[(3,4),(1,5)]])

        a = ComplexMatrix(a)
        b = ComplexMatrix(b)
        c = ComplexMatrix(c)
        try:
            a+b
            self.assertTrue(False)
        except:
            self.assertTrue(True)
            
    def test_deberia_multiplicar(self):
        
        a = ComplexMatrix.toComplexM([[(1,2),(2,1),(-3,5)],[(4,1),(0,1),(-2,3)]])
        b = ComplexMatrix.toComplexM([[(3,4),(1,2)],[(2,2),(4,7)],[(-1,3),(5,7)]])
        c = ComplexMatrix.toComplexM([[(-15,2),(-52,26)], [(-1,12),(-36,14) ]])
        
        a = ComplexMatrix(a)
        b = ComplexMatrix(b)
        c = ComplexMatrix(c)

        self.assertEqual(a*b,c)
    def test_no_deberia_multiplicar(self):
        
        a = ComplexMatrix.toComplexM([[(1,2),(4,5)],[(-5,4),(1,1)],[(1,3),(3,7)]])
        b = ComplexMatrix.toComplexM([[(3,2),(1,2)],[(-1,1),(3,3)]])

        a = ComplexMatrix(a)
        b = ComplexMatrix(b)
        try:
            a*b
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_deberia_ser_hermitiana(self):
        
        c = ComplexMatrix.toComplexM([[(3,0),(2,1)],[(2,-1),(1,0)]])
        
        c = ComplexMatrix(c)
        
        self.assertEqual(c,c.adj())

    def test_deberia_multiplicar_por_escalar(self):
        
        a = ComplexMatrix.toComplexM([[(3,2),(1,2)],[(-1,1),(3,3)]])
        b = ComplexMatrix.toComplexM([[(6,4),(2,4)],[(-2,2),(6,6)]])

        a = ComplexMatrix(a)
        b = ComplexMatrix(b)

        self.assertEqual(a*2,b)

    def test_deberia_unitaria(self):
        a = ComplexMatrix.toComplexM([[(1/(2**(1/2)),0),(0,1/(2**(1/2)))],[(0,1/(2**(1/2))),(1/(2**(1/2)),0)]])
        a = ComplexMatrix(a)

        self.assertTrue(a.esUnitaria())

    def test_distancia_0(self):
        a = ComplexMatrix.toComplexM([[(3,2),(1,2)],[(-1,1),(3,3)]])

        a = ComplexMatrix(a)

        self.assertEqual(0,a.distancia(a))


    
        
        


        
        
unittest.main()
