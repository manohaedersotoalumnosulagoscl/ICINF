lista=[]
cambio=950
for x in range(10):
    precio=float(input("Ingrese 10 precios de productos: "))
    lista.append(precio)
for x in range(len(lista)):
    lista[x]=lista[x]/cambio

print("A continuacion se mostrara el cambio de CLP a USD:", lista)