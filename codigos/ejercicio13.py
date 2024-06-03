"""13. Hacer un programa para el siguiente enunciado: Una aerolínea tiene proyectada la siguiente promoción: las
personas que viajen a Europa o África y son pasajeros frecuentes, acceden a un descuento de un 17% en el
valor de su pasaje. Además, los que van a Europa sean o no frecuentes reciben un descuento adicional. Los
pasajeros que viajan a cualquier punto de Egipto y son de tipo frecuente, tienen derecho a la compra de un
pasaje al mismo destino por un 50% de su valor. Los pasajeros que viajan fuera de Egipto pero dentro de África,
y no son del tipo frecuente, se les concede una cantidad de kilómetros gratuitos en su siguiente viaje. Los que
son o no son frecuentes y viajan a Europa, tienen derecho a una noche gratuita en un hotel de la ciudad
destino, y tienen el mismo derecho los que van a países de África (no Egipto) y son frecuentes."""

# las personas que viajen a Europa o África y son pasajeros frecuentes, acceden a un descuento de un 17% en el valor de su pasaje
#Los pasajeros que viajan a cualquier punto de Egipto y son de tipo frecuente, tienen derecho a la compra de un pasaje al mismo destino por un 50% de su valor.
#Los pasajeros que viajan fuera de Egipto pero dentro de África, y no son del tipo frecuente, se les concede una cantidad de kilómetros gratuitos en su siguiente viaje
#Los que son o no son frecuentes y viajan a Europa, tienen derecho a una noche gratuita en un hotel de la ciudad destino, y tienen el mismo derecho los que van a países de África (no Egipto) y son frecuentes.


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

