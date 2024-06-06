puntajes_diarios=[]

for d in range(1, 16):
    puntaje_diario=int(input("Ingrese el puntaje del día "+str(d)+": "))
    puntajes_diarios.append(puntaje_diario)

print("Días con puntaje mayor o igual a 70 puntos:")
for d in range(15):
    if puntajes_diarios[d]>=70:
        print("Día", d+1)

print("Días con puntaje menor a 70 puntos:")
for d in range(15):
    if puntajes_diarios[d]<70:
        print("Día", d+1)