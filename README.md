# Libreria con operaciones para matrices y vectores

Los numeros comples es la suma entre un número real y uno de tipo  **imaginario**  un número imaginario es aquél cuyo cuadrado es negativo. La librería que soportar por lo menos las siguientes operaciones de matrices con números complejos: Cada una de las funciones del programa recibe un par de matrices o una dependiendo de la función:

-   Adición de vectores complejos.
    
-   Inversa de vectores complejos.
    
-   Multiplicación escalar de vectores complejos.
    
-   Adición de matrices complejos.
    
-   Inversa de matrices complejos.
    
-   Multiplicación escalar de matrices complejas.
    
-   Matriz transpuesta
    
-   Matriz conjugada
    
-   Matriz adjunta
    
-   Función para calcular la "acción" de una matriz sobre un vector.
    
-   Norma de matrices
    
-   Distancia entrematrices
    
-   Revisar si es unitaria
    
-   Revisar si es Hermitian
    
-   Producto tensor.  _PARAMETROS_
## uso
    
m1,m2: ComplexMatrix, esta recibe una matriz compuesta de numeros complejos y tiene una funcion estatica (**toComplexM(matriz)**) para pasar de matrices de tuplas a matrices de numeros complejos 

cabe destacar que para usar la calculadora basta con importar el paquete de **ComplexMatrix** en un archivo python
    

1.  suma de matrices: m1+m2
    
    ```
    retorna la suma entre un par de martices de numeros complejos
    
    ```
2. multiplicacion: m1*m2
	 ```
    retorna la suma entre un par de martices de numeros complejos
    
    ```
    
3.  inversa: -m1
    
    ```
    retorna la matriz negativa
    
    ```
    
4.  Transpuesta: m1.transpuesta()
    
    ```
    retorna la transpuesta de la matriz 
    
    ```
    
5.  Conjugada: m1.conj()
    
    retorna la matriz Conjugada
    
   
    
6.  adjunta:  m1.anj()
    
    ```
    retorna la matriz Adjunta
    
    ```
    
7.  Accion: m1.accion(m2)
    
    ```
     retorna la  accion de una matriz
    
    ```
    
8.  norma: m1.norma()
    
    ```
    retorna la Norma de la matriz como un flotante
    
    ```
    
9.  Distancia: m1.distancia(m2)
    
    ```
    retorna la distancia entre un par de matrizes
    
    ```
    
11.  Unitario: m1.esUnitaria()
    
    ```
    retorna un Booleano dependiende de si la matriz es unitaria o no
    
    ```
    
11.  Hermitian: m1.hermitian()
    
    ```
    retorna un Booleano dependiende de si la matriz es Hermitian o no
    
    ```
    
12.  Producto Tensor: m1.ProductoTensor(m2)
    
    ```
    retorna el punto Tensor que es una nueva Matriz
    
    ```
    

## Lenguaje Programación

-   Python

## Pre-requisaitos

-   tener instalado python 3 o mayor
-   Si no tiene instalado python siga el siguiente tutorial  [https://es.wikihow.com/instalar-Python](https://es.wikihow.com/instalar-Python)

## Instalaciòn y ejecucion del proyecto

Descargue el repositorio lo puede realizar de dos formas descargando el .zip o usando git

En caso de usar git la linea de comando para clonar el repositiorio es:

```
git clone https://github.com/DamGaFlo/Calculator_CNYT

```
Este repositorio esta pensado para que sea importado y se usen sus respectivas operaciones, sin embargo se pueden hacer operaciones directamente en el archivo de la clase **complexMatrix**



## Ejecutar pruebas y aplicación

Para ejecutar las pruebas es necesario ejecutar el archivo diríjase al archivo test.py y testMatriz que se encuentra en la raiz del proyecto. - abrir la consola de comando entrar a la carpeta raiz y poner la siguiente linea de comando

MacOs o Linux

```
	- python3 test.py
	- python3 testMatriz.py

```

Windows

```
	- python test.py
	- python3 testMatriz.py

```
