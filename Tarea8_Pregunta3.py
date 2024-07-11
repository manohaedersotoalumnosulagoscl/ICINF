def separar(lista):
    par=[]
    impar=[]
    for n in lista:
        if n%2==0:
            par.append(n)
        else:
            impar.append(n)
    return sorted(par), sorted(impar)
pares, impares = separar([3,2,1,7,5,8,10,9])
print("Lista de los pares",pares)
print("Lista de los impares", impares)