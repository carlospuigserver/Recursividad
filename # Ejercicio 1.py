# Ejercicio 1



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





    
