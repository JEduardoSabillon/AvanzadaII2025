print("INGRESE LOS DATOS PARA CALCULAR SU DESCUENTO") 

precio = float(input("PRECIO: "))
descuento = float(input("DESCUENTO: "))

descuento = descuento / 100

print("EL PRECIO CON DESCUENTO ES: ", precio - (precio * descuento))
