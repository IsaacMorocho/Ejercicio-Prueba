print("************ Bienvenido al BURGER KING *************")
print("Ingrese los datos para su factura electronica")
#Variables
nombre = input("Ingrese su nombre:")
cedula = int(input("Ingrese su numero de cedula:"))
correo = input("Ingrese su correo electronico:")
n_hamburguesas = int(input("Ingrese el numero de hamburguesas a adquirir: "))
#Proceso de facturacion e impresion de resultados
print("Ingrese uno de los siguientes tipos de hamburguesas: 1, 2, 3")
print("1) Sencilla")
print("2) Doble")
print("3) Triple")
tp_hamb = int(input("Ingrese la opción: "))
if (tp_hamb==1 or tp_hamb==2 or tp_hamb==3):
    if tp_hamb==1:
        precio = n_hamburguesas * 1.50
    elif tp_hamb == 2:
        precio = n_hamburguesas * 2.50
    elif tp_hamb == 3:
        precio = n_hamburguesas * 3.25
    print("Ingrese su forma de pago: 1, 2, 3")
    print("1) Tajeta de crédito")
    print("2) Efectivo")
    pago = int(input("Ingrese la opción: "))
    if pago == 1:
        recargo = precio * 0.05
        total = precio + recargo
        print(f"Genial, {nombre} el precio final a pagar es: ${round(total,2)}")
        print(f"La factura se enviará a su correo: {correo}")
        print("********* Muchas gracias *********")
    elif pago == 2:
        print(f"Genial, {nombre} el precio final a pagar es: ${round(precio,2)}")
        print(f"La factura se enviará a su correo: {correo}")
        print("********* Muchas gracias *********")
    else:
        print("No existe ese tipo de pago")
        print("********* Muchas gracias *********")
else:
    print("Este tipo de hamburguesa no existe")
    print("******** Muchas gracias *********")

