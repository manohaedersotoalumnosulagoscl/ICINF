lista=[]
while True:
    x=input("Ingrese su palabra:")
    if x=="":
        break
    lista.append(x)

print("Ahora se mostrara la cantidad de letras a o A en cada palabra: ")
for palabra in lista:
    a=0
    for letra in palabra:
        if letra=="A" or letra=="a":
            a=a+1
    print(palabra+":"+str(a))