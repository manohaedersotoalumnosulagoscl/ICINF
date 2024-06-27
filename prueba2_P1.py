lista=[]
cantidad=0
suma=0
notas_baja=0
notas_altas=0
while True:
    nota=float(input("Ingrese las notas (ingrese 0 para terminar):"))
    if nota==0:
        break
    lista.append(nota)
    cantidad=cantidad+1
    suma=suma+nota
    if nota<4.0:
        notas_baja=notas_baja+1
    else:
        notas_altas=notas_altas+1
    
if cantidad>0:
    promedio=suma/cantidad
else:
    promedio=0

print("\nA continuacion se mostran los resultados:")
print("Cantidad de notas:", cantidad)
print("Promedio notas:", promedio)
print("Cantidad de notas bajas de 4.0:", notas_baja)
print("Cantidad de notas mayores o iguales a 4.0:", notas_altas)