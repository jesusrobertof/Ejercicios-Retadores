idProducto = [1, 2, 3]
producto = ["Maíz grano", "Pepino", "Tomate verde"]
costoPorCaja = [285.55, 334.72, 129.00]

numeroCajas = float(input ("Número de cajas a vender: "))
elegirProducto = int(input ("ID del producto: "))

if (numeroCajas <= 100):
    costoEnvio = 1500
else:
    costoEnvio = 0

if (elegirProducto == 1):
    print ("El producto es: " + producto[0])
    print ("El precio por caja es: " + str(costoPorCaja[0]))
    pagoTotal = (costoPorCaja[0]*numeroCajas) + costoEnvio
    print ("El costo total a pagar: ", pagoTotal)
elif (elegirProducto == 2):
    print ("El producto es: " + producto[1])
    print ("El precio por caja es: " + str(costoPorCaja[1]))
    pagoTotal = (costoPorCaja[1]*numeroCajas) + costoEnvio
    print ("El costo total a pagar: ", pagoTotal)
elif (elegirProducto == 3):
    print ("El producto es: " + producto[2])
    print ("El precio por caja es: " + str(costoPorCaja[2]))
    pagoTotal = (costoPorCaja[2]*numeroCajas) + costoEnvio
    print ("El costo total a pagar: ", pagoTotal)
else: 
    print("ID de producto no válido")