"""9. Realizar un programa que permita averiguar si un año es bisiesto. Considera que para que un año sea bisiesto
debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400."""
#la regla es si es divisible por 4 y no es divisible por 100 será un año bisiesto


year=int(input("Ingrese el año que desee consultar: "));
 
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("El año "+str(year)+" es bisiesto.");
else:
    print("El año "+str(year)+" no es bisiesto.")