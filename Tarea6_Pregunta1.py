def contar_vocales_consonantes(palabra):
    vocales="aeiouAEIOU"
    nvoc=0
    ncon=0

    for letra in palabra:
        if letra in vocales:
            nvoc=nvoc+1
        elif letra.isalpha():
            ncon=ncon+1
    
    return nvoc, ncon
palabras=[]
print("Ingresa la palabras. Para finalizar, ingresa una pabra vacia (presiona Enter).")
while True:
    palabra=input("Palabra: ")
    if palabra=="":
        break
    palabras.append(palabra)

for palabra in palabras:
    nvoc, ncon=contar_vocales_consonantes(palabra)
    print("Palabra:",palabra, "Vocales:",nvoc, "Consonantes:",ncon)