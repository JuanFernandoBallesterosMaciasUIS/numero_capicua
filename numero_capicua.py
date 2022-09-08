# Quiz: Leer un número entero de 5 digitos y determinar si es capicúa.

print("-------------------------------------")
print("-----DETECTOR-DE-NÚMERO-CAPICÚA------")
print("-------------------------------------")

#input
n = int(input("Por favor dígite un número de 5 dígitos: "))
#<>10000
if n >= 100000 or n <= 9999:
    print("")
    print("!!!ERROR!!! >>Digitaste un número diferente a 5 digitos<< !!!ERROR!!! ")
    print("")
    print("VUELVA A CORRER EL PROGRAMA")    
else:
    n1 = int(str(n)[::-1])
    if n1 == n:
        print("")
        print("------------------------------------")
        print("-------------RERSULTADO-------------")
        print("el número",n," es un número capicúa")
    else:
        print("")
        print("------------------------------------")
        print("-------------RERSULTADO-------------")
        print("el número",n,"no es un número capicúa")

