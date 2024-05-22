gasto=0
empleados=0
empleados2=0
while True:
    sueldo=int(input("Ingrese el sueldo del empleado (-1 para terminar): "))
    if sueldo==-1:
        break 

    if 500000<=sueldo<=900000:
        empleados=empleados+1
    elif sueldo>900000:
        empleados2=empleados2+1
    
    gasto=gasto+sueldo 
print("Empleados que cobran entre 500000 y 900000:", empleados)
print("Los empleados que cobran más de 900000:", empleados2)
print("Los gastos de la empresa son:", gasto)
