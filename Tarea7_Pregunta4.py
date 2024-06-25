deudores={}
contador=0

while contador<5:
    rut=input("Ingrese el rut del deudor:")
    deuda=float(input("Ingrese la deuda en pesos:"))
    deudores[rut]=deuda
    contador=contador+1

while True:
    rut_abono=input("Ingrese el rut del deudor que desea abonar (Ingrese Enter para finalizar)")
    if rut_abono=="":
        break
    abono=float(input("Ingrese el monto del abono:"))
    if rut_abono in deudores:
        deudores[rut_abono]-=abono
        if deudores[rut_abono]<=0:
            del deudores[rut_abono]

print("Deudores restantes y sus deudas:")
for rut in deudores:
    deuda=deudores[rut]
    print("Rut:", rut,", Deuda restante:", deuda, "pesos")