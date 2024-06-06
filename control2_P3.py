palabras=[]
while True:
    palabra=input("Ingrese una palabra (presione enter para finalizar): ")
    if palabra=="":
        break
    palabras.append(palabra)

if palabras:
    menor=len(palabras[0])
    for palabra in palabras[1:]:
        if len(palabra)<menor:
            menor=len(palabra)
    print("La palabra con la menor cantidad de caracteres tiene", menor, "caracteres.")

    