diccionario={}
contador=0

while contador<5:
    print("A continuancion debera elegir el pais y la capital que corresponda:")
    capital=input("Ingrese la capital:")
    pais=input("Ingrese el pais:")
    diccionario[capital]=pais
    contador=contador+1

nombre=input("Ingrese el nombre del turista:")
capitalt=input("Ingrese la capital del turista:")

for cap in diccionario:
    if cap==capitalt:
        paist=diccionario[cap]
        break
    

print("EL turista con el nombre",nombre,"viene de la capital",capitalt,"y su pais", paist)