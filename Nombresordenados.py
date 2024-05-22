nombre=input("Ingrese el nombre de la primera persona: ")
nombre2=input("Ingrese el nombre de la segunda persona: ")

orden=sorted((nombre,nombre2))
print("Nombres ordenados: ")
for nombres in orden:
    print(nombres)