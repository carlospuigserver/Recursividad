# Recursividad
### El link GitHub de este repositorio es: https://github.com/carlospuigserver/Recursividad.git

### Ejercicio 1: Busqueda por dicotomia en una tabla ordenada


* El código que he empleado para realizar este ejercicio es el siguiente:
```
tabla=input("Crea una tabla de números enteros mediante espacios:  ")
tabla= tabla.split() #Permite dividir una cadena de caracteres

for i in range(len(tabla)):
    tabla[i]= int(tabla[i])
    

caracter= input("Escribe que elemento de la tabla quieres buscar:  ")

# t = tabla   c = carácter  j = índice

def elemento(t,c,j):
    if c == str(t[j]):
        print("El elemento seleccionado está en la tabla")
    else:
        if j< (len(t)-1):
            j=+1
            elemento(t,c,j)
elemento(tabla,caracter,0)

```



### Ejercicio 2: Palíndromos
* El código que he empleado para realizar este ejercicio es el siguiente:

```
palabra=(input ("Escribe una palabra y vamos a analizar si es polindroma o no:  "))
p=len(palabra)
capicua=""

while p>0: 
    p=p-1
    capicua=capicua+palabra[p] #Concateno las letras una por una y las guardo
if palabra ==capicua:
        print("La palabra escogida es polindroma")
if palabra!= capicua:
        print("La palabra escogida no es polindroma")
 ```
 
 
 
 
 ### Ejercicio 3:  La bandera de Dijkstra
 * El código que he empleado para realizar este ejercicio es el siguiente:
 
 ```
 from random import randint
t=[]
i=0
fichas=["Verdes", "Azules", "Rojas"]
cantidad=int(input("Escribe con cuantas fichas quieres jugar:  "))
def tablero(t,i,fichas,cantidad):
    i+=1
    if i <= cantidad:
        t.append(fichas[randint(0,2)])
        tablero(t,i,fichas,cantidad)
tablero(t,i,fichas,cantidad)
print(t)

```
 

      
      








