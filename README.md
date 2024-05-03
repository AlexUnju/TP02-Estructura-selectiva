# TP02-Estructura-selectiva
## Casos de Estudio
Analice, diseñe y codifique los siguientes enunciados en Python
### 1. Una institución de educación, con regímenes tanto diurnos como vespertinos, considera lo siguiente en su proceso académico: 
si un estudiante de régimen vespertino tiene una nota de presentación mayor o igual a 6,
se exime, y si no alcanza el 6 pero tiene una nota de presentación igual o mayor a 3.5, rinde examen. Si el
estudiante es de régimen diurno, si su nota de presentación es mayor o igual a 3.5, rinde examen (no hay
posibilidad de eximirse). En ambos regímenes, si la nota de presentación es menor que 3.5, reprueba. Hacer la
tabla de decisión y escriba el algoritmo correspondiente.

#### Resolución:
```python
notaEstudiante = float(input("Ingrese la nota del estudiante: "));
regimen= int(input("Ingrese el régimen del estudiante: 1) diurno o 2) vespertino : "));

if regimen == 1:
        if notaEstudiante > 3.5:
                print("El estudiante de regimen "+str(regimen)+ " rinde examen");
        else: 
                print("El estudiante de regimen "+str(regimen)+ " ha reprobado");
elif regimen == 2:
        if notaEstudiante > 6:
                print("el estudiante de regimen "+str(regimen)+ " se exime del examen");
        elif notaEstudiante > 3.5 and notaEstudiante <= 6:
                print("El estudiante de regimen "+str(regimen)+ " rinde examen");
        else:
                print("El estudiante de regimen "+str(regimen)+ " ha reprobado");	
```
###

## Ejercicios
### 1. Si r = 10, s = 0, resolver mostrando el orden de los pasos la siguiente expresión lógica:
```python
(r != 10) or not (s == -r) or not((True or r >= 10) and not (s <= 0 and True))
```
#### Resolución:
```python
"(r != 10) or not (s == -r) or not((True or r >= 10) and not (s <= 0 and True))"
" false    or       true    or not(true and false)"
"false      or      true    or true"
"true or true"
"true"

r=10;
s=0;

verificacion= (r != 10) or not (s == -r) or not((True or r >= 10) and not (s <= 0 and True));
print(verificacion);
```
##
### 2. Dadas v, w, z variables de tipo numérico entero escribir las expresiones lógicas correspondientes a los siguientes enunciados:
A. v es no positivo y w es no menor o igual a cero.
B. v, w, z son diferentes entre sí.
C. v es no nulo y w no es mayor a z.
D. w está estrictamente entre v y z.
E. v es igual a w o z es no negativo pero no ambos a la vez.

#### Resolución:
```python
v=5;
w=10;
z=15;

verificacionA= v <= 0 and w >= 0;
verificacionB= v != w and v != z and w != z;
verificacionC= v != 0 and not(w > z);
verificacionD= v<w<z or z<w<v;
verificacionE= v==w or z >= 0 and not(v==w or z>=0);
```

##
### 3. Analice el siguiente código en Python:
```python
clave = "iprog1"
contraseña = input("Introduce la contraseña: ")
if clave == contraseña:
  print("La contraseña coincide")
else:
  print("La contraseña NO coincide")
```
- **¿Cuándo se visualizará en la pantalla el mensaje “coincide”?**
  - El mensaje "coincide" se visualizará en la pantalla cuando la contraseña ingresada por el usuario coincida exactamente con la clave definida en el código, es decir, cuando `contraseña` sea igual a `"iprog1"`.

- **Si ingresa en la variable contraseña iProg1, ¿Qué mensaje se verá en la pantalla?**
  - Si se ingresa en la variable `contraseña` el valor `"iProg1"` (o cualquier variante de mayúsculas y minúsculas), el mensaje "La contraseña NO coincide" se visualizará en la pantalla, ya que la comparación de cadenas es sensible a mayúsculas y minúsculas y la contraseña no coincidirá exactamente con la clave definida.

- **Mejore la sentencia en la línea 3 utilizando alguna función que salve la situación anterior.**
  ```python
  clave = "iprog1"
  contraseña = input("Introduce la contraseña: ")
  if clave.lower() == contraseña.lower():
    print("La contraseña coincide")
  else:
    print("La contraseña NO coincide")```
- **¿Qué sucede si ingresa un número?**
  - Si se ingresa un número en lugar de una cadena para la contraseña, el programa continuará ejecutándose sin errores, pero la comparación `clave == contraseña` probablemente dará como resultado `False`, ya que la contraseña ingresada no coincidirá con la clave de cadena. Esto provocará que se imprima "La contraseña NO coincide".

##
### 4. Escribir el código en python que permita el registro de la edad del cliente y la cantidad de fichas que compra en una sala de juegos para niños. 
El programa debe mostrar el monto total de la fichas compradas teniendo en
cuenta que si la edad está en el intervalo [4,7) el precio de las fichas es un 20% más barata y además reciben 5
fichas gratis, si la edad está en el intervalo [7,10) el precio de las fichas es un 15% más cara. Para edades fuera
de esos rangos no se permite el ingreso a la sala de juegos. El precio unitario de las fichas no varía y es de 35
pesos.

#### Resolución:
```python
edadCliente= int(input("ingrese la edad :"));
cantidadFichas= int(input("ingrese la cantidad de fichas a comprar: "));
precioFichas=35


if 4 <= edadCliente < 7:
    descuento=(precioFichas*20)/100
    print((precioFichas-descuento)*cantidadFichas);
elif 7<= edadCliente < 10:
    aumento=(precioFichas*15)/100;
    print(aumento)
    print((precioFichas+aumento)*cantidadFichas);
else:
    print("no se permite el ingreso")
```
##

### 5. Diseñar un algoritmo que permita leer 3 números y escribir en la pantalla si están en “orden creciente” o “decreciente” o “no están en orden”.
#### Resolución:
```python
num1=int(input("ingrese un número: "));
num2=int(input("ingrese un segundo número: "));
num3=int(input("ingrese un tercer número: "));

if num1 < num2 < num3:
    print("los números están en orden creciente");
elif num1 > num2 > num3:
    print("los números estan en orden decreciente");
else:
    print("los números no tienen orden");
```
##
### 6. Diseñar un algoritmo que ordene en forma creciente tres valores diferentes a, b, c
#### Resolución:
```python
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
```
##
### 7. Sin ejecutar el código en la computadora, ingresando primero “a” y luego “v” debe mostrar todas las salidas en la pantalla.
```python
print("Este programa mezcla dos colores.")
print(" r. Rojo a. Azul")

primera = input(" Elija un color (r o a): ")

if primera == "r":
    print(" a. Azul v. Verde")
    segunda = input(" Elija otro color (a o v): ")
    if segunda == "a":
        print("La mezcla de Rojo y Azul producen Magenta.")
    else:
        print("La mezcla de Rojo y Verde producen Amarillo.")
else:
    print(" v. Verde r. Rojo")
    segunda = input(" Elija otro color (v o r): ")
if segunda == "v":
    print("La mezcla de Azul y Verde producen Cian.")
else:
        print("La mezcla de Azul y Rojo producen Magenta.")
print("¡Hasta la próxima!")
```
#### Resolución:
```python
#este programa mezcla colores
#r.rojo a.azul

#print verde y rojo
# la mezcla de azul y verde producen Cian

#hasta la proxima
```
##
### 8. Sin ejecutar el código en la computadora, ¿Cuál es la salida por la pantalla? Para los siguientes valores:
<img src="https://i.ibb.co/svdXBCr/Screenshot-2024-05-03-133218.png" alt="Screenshot-2024-05-03-133218" border="0"><br>
#### Resolución:
```python
#Es un niño
#Es un adolescente
```
##
### 9. Realizar un programa que permita averiguar si un año es bisiesto. Considera que para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
#### Resolución:
```python
year=int(input("Ingrese el año que desee consultar: "));
 
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("El año "+str(year)+" es bisiesto.");
else:
    print("El año "+str(year)+" no es bisiesto.")
```
##
### 10. Diseñar dos programas que utilicen la sentencia selectiva simple y la sentencia encadenada if…elif…else…, el programa debe pedir la edad y en función del valor recibido mostrará un mensaje diferente.
- si el valor de la edad es negativo, se trata de un error
- si el valor de la edad está entre 0 y 17, se trata de un menor de edad
- si el valor de la edad es superior o igual a 18, se trata de un mayor de edad
#### Resolución:
```python
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
```
##
11. Hacer dos programas que utilicen la sentencia selectiva compuesta (anidada) y la sentencia if…elif…else…, el programa debe pedir un número y mostrará:
- si es múltiplo de dos,
- si es múltiplo de cuatro (y de dos)
- si no es múltiplo de dos
Nota: El valor 0 se considerará múltiplo de 4 y de 2.
#### Resolución:
```python
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
```
##
### 12. Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: 
los lunes se dicta el Nivel Inicial, los martes el Nivel Intermedio, los
miércoles el Nivel Avanzado, los jueves son para Práctica Hablada y los viernes se dicta Inglés para Viajeros.
El usuario ingresa la fecha actual en formato “día, DD/MM", donde [día] es un día de la semana
(lun-mar-mie-jue-vie), DD es el número de día y MM es el número de mes. Si el usuario ingresa un día de la
semana inexistente o una fecha cuyo día supere el rango 1-31 o el mes de 1 a 12, indique que se produjo un
error. Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente.
Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se
trata de los niveles Inicial, Intermedio o Avanzado, ya que las Prácticas Habladas y el Inglés para Viajeros no
tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el
programa le mostrará el porcentaje de Aprobados.
Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a
clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la
mayoría" si no es así.
Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 de cualquier mes, se deberá imprimir
"Comienzo de nuevo ciclo".

#### Resolución:
```python
diaSemana=str(input("Ingrese el día de la semana [lun,mar,mie,jue,vie,] : "));
dia=int(input("Ingrese una fecha del [1-31]: "));
mes=int(input("Ingrese un mes[1-12]: "));
diaSemana = diaSemana.lower()

if diaSemana == "lun":
    print("¿se tomaron examen el día "+ diaSemana+"?");
    examen=str(input("Ingrese: Si o No: "));
    if examen.upper() == "SI":
        alumAprobados=int(input("Ingrese cuantos alumnos aprobaron: "));
        alumDesaprobados=int(input("Ingrese cuantos alumnos desaprobaron: "));
        porcentajeAprobados=(alumAprobados/(alumAprobados+alumDesaprobados))*100;
        print("El porcentaje de alumnos desaprobados del Nivel Inicial del examen del día ", diaSemana, " es de: ", round(porcentajeAprobados,0), "%");
elif diaSemana == "mar":
    print("¿se tomaron examen el día "+ diaSemana+"?");
    examen=str(input("Ingrese: Si o No: "));
    if examen.upper() == "SI":
        alumAprobados=int(input("Ingrese cuantos alumnos aprobaron: "));
        alumDesaprobados=int(input("Ingrese cuantos alumnos desaprobaron: "));
        porcentajeAprobados=(alumAprobados/(alumAprobados+alumDesaprobados))*100;
        print("El porcentaje de alumnos desaprobados del Nivel Medio del examen del día ", diaSemana, " es de: ", round(porcentajeAprobados,0), "%");
elif diaSemana== "mie":
    print("¿se tomaron examen el día "+ diaSemana+"?");
    examen=str(input("Ingrese: Si o No: "));
    if examen.upper() == "SI":
        alumAprobados=int(input("Ingrese cuantos alumnos aprobaron: "));
        alumDesaprobados=int(input("Ingrese cuantos alumnos desaprobaron: "));
        porcentajeAprobados=(alumAprobados/(alumAprobados+alumDesaprobados))*100;
        print("El porcentaje de alumnos desaprobados del Nivel Avanzado del examen del día ", diaSemana, " es de: ", round(porcentajeAprobados,0), "%");

elif diaSemana== "jue":
    asistencia=int(input("Ingrese el porcentaje de su asistencia a clase: "));
    if asistencia > 50:
        print("El estudiante de ",diaSemana, " de practica hablada asistió la mayoría.");
    else:
        print("El estudiante de ",diaSemana, " de practica hablada no asistió la mayoría.");

elif diaSemana == "vie":
    if dia == 1:
        print("COmienza un nuevi ciclo:")
    else:
        print("un dia normal mi crack uwu")
else:
    print("Error al ingresar la fecha")
```
##
### 13. Hacer un programa para el siguiente enunciado: Una aerolínea tiene proyectada la siguiente promoción: 
las
personas que viajen a Europa o África y son pasajeros frecuentes, acceden a un descuento de un 17% en el
valor de su pasaje. Además, los que van a Europa sean o no frecuentes reciben un descuento adicional. Los
pasajeros que viajan a cualquier punto de Egipto y son de tipo frecuente, tienen derecho a la compra de un
pasaje al mismo destino por un 50% de su valor. Los pasajeros que viajan fuera de Egipto pero dentro de África,
y no son del tipo frecuente, se les concede una cantidad de kilómetros gratuitos en su siguiente viaje. Los que
son o no son frecuentes y viajan a Europa, tienen derecho a una noche gratuita en un hotel de la ciudad
destino, y tienen el mismo derecho los que van a países de África (no Egipto) y son frecuentes.

#### Resolución:
```python
viaje=int(input("Ingrese el destino Europa: \n 1) Europa \n 2) Africa \n"));
pasajeroFrecuente=str(input("el pasajero es frecuente? [si, no] "));

if viaje == 1 or viaje == 2:
    if pasajeroFrecuente == "si":
        print(" \n El pasajero destino a Europa y si frecuente recibe un descuento del 17% en el valor de su pasaje \n")
    elif pasajeroFrecuente == "no" and viaje==1:
        print("el pasajero de destino a Europa pero no frecuente recibe un descuento adicional");
    if pasajeroFrecuente == "si" or pasajeroFrecuente == "si" and viaje==1:
        print("tiene derecho a una noche gratis en un hotel")
if viaje == 2:
    puntoViaje=int(input("Ingrese el punto de destino \n 1) egipto \n 2) otro: \n") );
    if puntoViaje == 1 and pasajeroFrecuente == "si":
      print("El pasajero destino africa y a Egipto recibe un 50% de descuento en su pasaje")
    elif puntoViaje == 2:
        if pasajeroFrecuente == "no":
            print("El pasajero destino a otro tiene derecho de tener kilometros gratuitos en su siguiente destino")
    if puntoViaje == 2 and pasajeroFrecuente=="si":
        print("tiene derecho a una noche gratis en un hotel")
```
##
### 14. Hacer un programa para el siguiente enunciado: El proceso de inscripción de estudiantes de un instituto se efectúa de la siguiente manera: 
si el estudiante es nuevo, debe llenar una ficha de inscripción con sus datos.
Además, debe pagar un derecho de incorporación, a menos que tenga algún tipo de beca autorizada. Todos los
estudiantes, antiguos y nuevos, deben cancelar un valor por concepto de matrícula antes de una cierta fecha
límite. Si el estudiante paga dentro de tal plazo, se inscribe en las asignaturas. Si lo hace fuera del plazo
establecido, deberá elevar una solicitud. Dependiendo de los motivos que el estudiante tuvo para pagar la
matrícula fuera del plazo, la solicitud podrá ser aprobada o rechazada. Si es rechazada, quedará fuera del
proceso y perderá los valores que hubiera cancelado. Si es aceptada, podrá efectuar su inscripción de
asignaturas, previo pago de una multa, de la cual están exentos los estudiantes nuevos.
#### Resolución:
```python
estudiante=str(input("El estudiante es: \nNuevo \nAntiguo \n"));
estudiante = estudiante.lower();

if estudiante == "nuevo" or estudiante == "antiguo":
    #nuevo
    if estudiante == "nuevo":
        print("El estudiante "+estudiante+" debe llenar una ficha de inscripción con sus datos");
        beca=str(input("¿Tiene Beca autorizada? si - no: "));
        if beca == "si":
            print("El estudiante no paga la incorporacion");
        elif beca == "no":
            print("el alumno debe pagar un derecho de incorporación.")
    #antiguo o nuevo
    if estudiante == "antiguo" or "nuevo":
        print("El estudiante "+estudiante+" debe cancelar un valor por concepto de matrícula antes del plazo limite")
        pagoFechaLimite=str(input("¿El estudiante pago dentro del plazo? si - no : "));
        if pagoFechaLimite == "si":
            print("El estudiante"+estudiante+" se inscribe a las asignaturas.");
        elif pagoFechaLimite == "no":
            print("El estudiante "+estudiante+" deberá elevar una solicitud");
            if pagoFechaLimite == "no":
                solicitud=str(input("Ingrese su motivo: problema o descuido : "));
                if solicitud == "problema":
                    if estudiante == "nuevo":
                        print("El estudiante:"+estudiante+" puede efectuar su inscripción a sus asignaturas y queda exentuado de pagar la multa");
                    elif estudiante == "antiguo":
                        print("El estudiante "+estudiante+" fué aprobado y puede efectuar su inscripción a sus asignaturas, previo pago de una multa.");
                if solicitud == "descuido":
                        print("El estudiante "+estudiante+" fué rechazado y quedará fuera del proceso y perderá los valores que hubiera cancelado")
else: 
    print("error al ingresar el dato.")
```






