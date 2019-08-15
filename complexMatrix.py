from complejo import Complejo


class ComplexMatrix():
    # m y n son las dimenciones de la matriz
    
    def __init__(self,datos):
        self.m = len(datos);
        self.n = len(datos[0]);
        self.datos = datos;

    def getStr(self):
        for i in datos:
            for j in i:
                print(j.getStr()+" ",end="")


    def suma(self, value):
        if self.n != value.n or self.m != value.m:
            raise TypeError("las dimensiones deben ser iguales");
        datos = []
        for i in range(self.m):
            datos.append([]);
            for j in range(self.n):
                datos.append(self.datos[i][j].suma(value.datos[i][j]));


def main():
    a = [[(1,2),(3,4)],[(-5,7),(8,1)],[(-1,-1),(0,13)],[(10,5),(3,2)]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = Complejo(a[i][j][0],a[i][j][1])
    
main()
    
                
                
            
        
        
            
        
    
        
