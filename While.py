i = 0
while i < 10:
    print(i)
    i += 1

#print ("ciclo controlado por banderin")
#while True:
#    entrada = input("ingrese 5 para salir ")
#   if entrada.upper == "5":
#        break
    
#    print ("ciclo controlador por banderin 2")
#    bandera= "X"
#    while bandera != "5":
#        bandera = input("ingrese 5 para salir ")

print ("ciclo controlado por banderin")
bandera = True
while bandera != False:
    bandera = input("ingrese 5 para salir ")
    print (bandera.upper)
    salir =bandera.upper()
    if salir == "5":
        bandera = False
        print ("saliste del ciclo")