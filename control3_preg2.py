def es_binario(var):
    for x in var:
        if x!= "1" and x!="0":
            return False
    return True

print(es_binario("100010101010101"))
print(es_binario("123242"))
print(es_binario("101"))


