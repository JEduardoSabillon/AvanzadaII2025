import os
os.system('cls' if os.name == 'nt' else 'clear')

# ciclo for
#for i in range(10):
#   print(i)    

#RANGER(INICIO, FIN, CRECIMIENTO)    
#for i in range(2, 22, 2):
#    print(i) 

#ciclo for con lista
lista =["uno", "dos", "tres", "cuatro", "cinco"] 
for item in lista:
    print(item)      

#INvertir el orden de las listas 
for item in reversed(lista):
    print(item)     
    
#Ciclo for con tuplas
#tuple=("unos", "dos", "tres", "cuatro", "cinco")
#for item in tuple:
#    print(item)
    
#ciclo for con diccionario
#diccionario = {
#    "curso":"python Total",
#   "clase":"Ciclos",
#    "temas":"for",
#   "duracion":"trimestre",
#    "Profesor":"Jose Eduardo"
#}   
#print(diccionario) 
#for llave in diccionario:
#    print(llave, diccionario[llave])     