"""14. Hacer un programa para el siguiente enunciado: El proceso de inscripción de estudiantes de un instituto se
efectúa de la siguiente manera: si el estudiante es nuevo, debe llenar una ficha de inscripción con sus datos.
Además, debe pagar un derecho de incorporación, a menos que tenga algún tipo de beca autorizada. Todos los
estudiantes, antiguos y nuevos, deben cancelar un valor por concepto de matrícula antes de una cierta fecha
límite. Si el estudiante paga dentro de tal plazo, se inscribe en las asignaturas. Si lo hace fuera del plazo
establecido, deberá elevar una solicitud. Dependiendo de los motivos que el estudiante tuvo para pagar la
matrícula fuera del plazo, la solicitud podrá ser aprobada o rechazada. Si es rechazada, quedará fuera del
proceso y perderá los valores que hubiera cancelado. Si es aceptada, podrá efectuar su inscripción de
asignaturas, previo pago de una multa, de la cual están exentos los estudiantes nuevos.
"""


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


