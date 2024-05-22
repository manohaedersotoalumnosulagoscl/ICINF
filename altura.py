suma=0
personas=0
while True:
    x=float(input("Ingresela altura (Ingrese 0 si quiere finalizar)"))
    if x==0:
        break
    suma=suma+x   
    personas=personas+1     
if personas>0:
    promedio=suma/personas
    print("La altura promedio de las personas es:", promedio)