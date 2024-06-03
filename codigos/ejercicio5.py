"""5. Diseñar un algoritmo que permita leer 3 números y escribir en la pantalla si están en “orden creciente” o
“decreciente” o “no están en orden”.
"""

num1=int(input("ingrese un número: "));
num2=int(input("ingrese un segundo número: "));
num3=int(input("ingrese un tercer número: "));

if num1 < num2 < num3:
    print("los números están en orden creciente");
elif num1 > num2 > num3:
    print("los números estan en orden decreciente");
else:
    print("los números no tienen orden");