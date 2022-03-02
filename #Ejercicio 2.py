#Ejercicio 2

palabra=input ("Escribe una palabra a analizar:  ")
capicua=""
p=len(palabra)

while p>=0: #Concateno las letras una por una y las guardo
    p=p-1
    capicua=capicua+palabra[p]
if palabra ==capicua:
        print("Es polindroma")
else:
        print("No lo es")