from complejo import Complejo


class ComplexMatrix():
    # m y n son las dimenciones de la matriz
    
    def __init__(self,datos):
        self.m = len(datos);
        self.n = len(datos[0]);
        self.datos = datos;
    def __str__(self):
        representacion =""
        for i in self.datos:
            for j in i:
                representacion += str(j)+" "
            representacion += "\n"
        return representacion;



    def __add__(self, value):
        if self.n != value.n or self.m != value.m:
            raise TypeError("las dimensiones deben ser iguales");
        datos = []
        for i in range(self.m):
            datos.append([]);
            for j in range(self.n):
                datos[i].append(self.datos[i][j]+value.datos[i][j]);
        
        return ComplexMatrix(datos);
    def __mul__(self,value):
        if  self.n != value.m:
            raise TypeError("las dimensiones deben ser iguales");
        mat = []
        for i in range(self.m):
            mat.append([])
            for j in range(value.n):
                suma = Complejo(0,0)
                for k in range(self.m):
                    suma += self.datos[i][k]*value.datos[k][j]
                mat[-1].append(suma)
        return ComplexMatrix(mat)
                    
        
        
    


def main():
    a = [[(1,0),(2,0),(-3,0)],[(4,0),(0,0),(-2,0)]]
    b = [[(3,0),(1,0)],[(2,0),(4,0)],[(-1,0),(5,0)]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = Complejo(a[i][j][0],a[i][j][1])
            
    for i in range(len(b)):
        for j in range(len(b[0])):
            b[i][j] = Complejo(b[i][j][0],b[i][j][1])
            
    matriz = ComplexMatrix(a)
    matriz2 = ComplexMatrix(b)
    print(matriz*matriz2)
    
    
main()
            
        
    
        
