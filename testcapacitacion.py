preguntas=int(input("Ingrese la cantidad de preguntas que se le realizaron: "))
correctas=int(input("Ingrese la cantidad de preguntas correctas: "))
porcentaje= (correctas/preguntas)*100

if porcentaje>=95:
    print("Nivel maximo")
else:
    if porcentaje>=70 and porcentaje<95:
        print("Nivel medio")
    else:
        if porcentaje>=40 and porcentaje<70:
            print("Nivel regular")
        else:
            print("Fuera de nivel")
