from complejo import Complejo


class ComplexMatrix():
    # m y n son las dimenciones de la matriz
    
    def __init__(self,datos):
        #m=filas
        self.filas = len(datos);
        self.columnas = len(datos[0]);
        self.datos = datos;
        
    def __neg__(self):
        return self*-1;
    
    def __str__(self):
        representacion =""
        for i in self.datos:
            for j in i:
                representacion += str(j)+" "
            representacion += "\n"
        return representacion;

    
    def __eq__(self,matriz):
        if matriz.columnas == self.columnas and matriz.filas == self.filas:
            for i in range(matriz.filas):
                for j in range(matriz.columnas):
                    if(matriz.datos[i][j] != self.datos[i][j]):
                        return False;
            return True;
        return False;
        



    def __add__(self, value):
        if self.comunas != value.columnas or self.filas != value.filas:
            raise TypeError("las dimensiones deben ser iguales");
        datos = []
        for i in range(self.filas):
            datos.append([]);
            for j in range(self.columnas):
                datos[i].append(self.datos[i][j]+value.datos[i][j]);
        
        return ComplexMatrix(datos);
    
    def __mul__(self,value):
        if(type(value)==int):
            return value*self;
        if  self.columnas != value.filas:
            raise TypeError("las dimensiones deben ser iguales");
        mat = []
        for i in range(self.filas):
            mat.append([])
            for j in range(value.columnas):
                suma = Complejo(0,0)
                for k in range(self.columnas):
                    suma += self.datos[i][k]*value.datos[k][j]
                
                mat[-1].append(suma)
        return ComplexMatrix(mat)
    
    def __rmul__(self,value):
        datos = []
        for i in self.datos:
            datos.append([])
            for j in i:
                datos[-1].append(value*j)
        return ComplexMatrix(datos);
                    
        
        
    def transpuesta(self):
        datos = []
        for i in range(self.columnas):
            datos.append([])
            for j in range(self.filas):
                datos[-1].append(self.datos[j][i])
        return ComplexMatrix(datos);
    def conj(self):
        datos = []
        for i in self.datos:
            datos.append([])
            for j in i:
                datos[-1].append(j.conj())
        return ComplexMatrix(datos);
    def adj(self):
        return self.transpuesta().conj();
    def trace(self):
        if(self.filas!=self.columnas):
            raise TypeError("las dimensiones deben ser iguales");
        suma = Complejo(0,0); 
        for i in range(self.filas):
            suma+=self.datos[i][i];
        return suma;
    def norma(self):
        return ((self.adj()*self).trace().getReal())**(1/2)
            
            


def main():
    a = [[(1,0),(2,0),(-3,0)],[(4,0),(0,0),(-2,0)]]
    b = [[(3,0),(1,0)],[(2,0),(4,0)],[(-1,0),(5,0)]]
    c = [[(3,0),(2,1)],[(2,-1),(1,0)]]
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = Complejo(a[i][j][0],a[i][j][1])
            
    for i in range(len(b)):
        for j in range(len(b[0])):
            b[i][j] = Complejo(b[i][j][0],b[i][j][1])

    for i in range(len(c)):
        for j in range(len(c[0])):
            c[i][j] = Complejo(c[i][j][0],c[i][j][1])
            
    matriz = ComplexMatrix(a)
    matriz2 = ComplexMatrix(b)
    ma = ComplexMatrix(c)

    print(ma == ma.adj())
    
    print(matriz.norma())
    print("")
    print(matriz2)
    print("")
    print(matriz*matriz2)
    
    
main()
            
        
    
        
