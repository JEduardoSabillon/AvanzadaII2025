import os
os.system('cls' if os.name == 'nt' else 'clear')

#condicional.if
edad=int(input("Ingresa tu edad: "))
if edad >= 21:
    print("eres mayor de edad")
elif edad >= 18:
    print("eres ciudadano")
else:
    print("eres menor de edad")
