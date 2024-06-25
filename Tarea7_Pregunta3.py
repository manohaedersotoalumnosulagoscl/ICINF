supermercado={}

while True:
    producto=input("Ingrese el nombre del producto (seleccione Enter para finalizar:) ")
    if producto=="":
        break
    cantidad=int(input("Ingrese la cantidad del producto:"))
    supermercado[producto]=cantidad

x=int(input("Ingrese el valor para multiplicar las cantidades:"))
print("Productos multiplicados por",x,":")

for producto in supermercado:
    cantidad=supermercado[producto]
    print(producto+":"+str(cantidad*x))