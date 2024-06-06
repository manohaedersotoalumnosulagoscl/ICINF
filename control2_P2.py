nombres=[]
for i in range(7):
    nombre=input("Ingrese un nombre: ")
    nombres.append(nombre)

sina=[]
for nombre in nombres:
    if nombre[-1]!="a":
        sina.append(nombre)

nombres=sina

print("Lista despues de la eliminacion de nombres que terminen en a:")
print(nombres)