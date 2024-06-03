"""Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones
sobre las clases de ese día. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases
en un día de la semana diferente: los lunes se dicta el Nivel Inicial, los martes el Nivel Intermedio, los
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
"Comienzo de nuevo ciclo"."""

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
