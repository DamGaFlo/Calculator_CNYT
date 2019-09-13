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
        if self.columnas != value.columnas or self.filas != value.filas:
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
    
    def toComplexM(mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = Complejo(mat[i][j][0],mat[i][j][1])
        return mat;

    def esUnitaria(self):
        error = 0.000000000001
        value = self*self.adj()

        for i in range(value.filas):
            for j in range(value.columnas):
                if i==j:
                    if not(value.datos[i][j].real-1<=error and value.datos[i][j].real-1>=-error):
                        
                        return False;
                else:
                    if not(value.datos[i][j].real<=error and value.datos[i][j].real>=-error):
                        return False;
        return True;

    def distancia(self,value):
        try:
            return (self+-value).norma()
        except:
            raise TypeError("no se puede hayar la distancia entre estas 2 matrices");
    def hemitian(self):
        return self==self.adj()

            
            



    
        
