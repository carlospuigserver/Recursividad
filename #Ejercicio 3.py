#Ejercicio 3

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