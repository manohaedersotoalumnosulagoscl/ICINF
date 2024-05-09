n=0
cont=0
while n>=0:
    n=int(input("Ingrese un numero: "))
    if n<0:
        break
    cont=cont+1

print("Se ingresaron", cont, "numeros... ")