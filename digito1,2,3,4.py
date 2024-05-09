n1=int(input("Ingre un numero del 1 al 9999: "))
if n1>=1 and n1<10:
    print("Su numero contiene un digito")
else:   
    if n1>=10 and n1<=99:
        print("Su numero contiene dos digito")
    else:
        if n1>=100 and n1<=999:
            print("Su numero contiene tres digitos")
        else:
            if n1>=1000 and n1<=9999:
                print("Su numero contiene cuatro digitos")
