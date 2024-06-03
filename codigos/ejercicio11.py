"""11. Hacer dos programas que utilicen la sentencia selectiva compuesta (anidada) y la sentencia if…elif…else…, el
programa debe pedir un número y mostrará:
● si es múltiplo de dos,
● si es múltiplo de cuatro (y de dos)
● si no es múltiplo de dos
Nota: El valor 0 se considerará múltiplo de 4 y de 2."""

numero=int(input("ingrese un número: "));

if numero % 2 == 0:
    if numero % 4==0:
        print("es multiplo de 4 y 2")
    else:
        print("es multiplo de 2 pero no es multiplo de 4")
else:
    print("no es multiplo de 2")

#segundo programa:

if 4 == 0 or numero == 0:
    print("es multiplo de 4 y de 2");
elif numero % 2==0:
    print("es multiplo de 2")
else:
    print("no es multiplo de 2")
