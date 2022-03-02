#Ejercicio 2

palabra=input ("Escribe una palabra y vamos a analizar si es polindroma o no:  ")
p=len(palabra)
capicua=""

while p>0: 
    p=p-1
    capicua=capicua+palabra[p] #Concateno las letras una por una y las guardo
if palabra ==capicua:
        print("La palabra escogida es polindroma")
if palabra!= capicua:
        print("La palabra escogida no es polindroma")