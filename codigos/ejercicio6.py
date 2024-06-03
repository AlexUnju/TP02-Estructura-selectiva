"""6. Diseñar un algoritmo que ordene en forma creciente tres valores diferentes a, b, c
"""


num1=int(input("ingrese un número: "));
num2=int(input("ingrese un segundo número: "));
num3=int(input("ingrese un tercer número: "));
#43223
#721 b 
#7823 c

if num1 > num2:
    num1 , num2 = num2,num1
if num2 > num3:
    num2, num3= num3,num2;
if num1>num2:
    num1,num2= num2,num1;
print("Los valores ordenados en forma creciente son:", num1, num2, num3)

