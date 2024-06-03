"""10. Diseñar dos programas que utilicen la sentencia selectiva simple y la sentencia encadenada if…elif…else…, el
programa debe pedir la edad y en función del valor recibido mostrará un mensaje diferente.
● si el valor de la edad es negativo, se trata de un error
● si el valor de la edad está entre 0 y 17, se trata de un menor de edad
● si el valor de la edad es superior o igual a 18, se trata de un mayor de edad"""

edad=int(input("ingrese su edad: "));

#primer programa

if edad < 0:
    print("Error, la edad es un número negativo");
if 0 <= edad <= 17:
    print("Se trata de un menor de edad");
if edad >= 18:
    print("se trata de un mayor de edad");
 
#segundo programa
if edad < 0:
    print("Error, el número es negativo");
elif 0 <= edad <= 17:
    print("se trata de un menor de edad");
else:
    print("se trata de un mayor de edad");