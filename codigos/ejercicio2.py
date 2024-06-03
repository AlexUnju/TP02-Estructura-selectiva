"""2. Dadas v, w, z variables de tipo numérico entero escribir las expresiones lógicas correspondientes a los
siguientes enunciados:
A. v es no positivo y w es no menor o igual a cero.
B. v, w, z son diferentes entre sí.
C. v es no nulo y w no es mayor a z.
D. w está estrictamente entre v y z.
E. v es igual a w o z es no negativo pero no ambos a la vez.
"""
v=5;
w=10;
z=15;

verificacionA= v <= 0 and w >= 0;
verificacionB= v != w and v != z and w != z;
verificacionC= v != 0 and not(w > z);
verificacionD= v<w<z or z<w<v;
verificacionE= v==w or z >= 0 and not(v==w or z>=0);
