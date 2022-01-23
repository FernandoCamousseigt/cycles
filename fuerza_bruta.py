#option1
from string import ascii_lowercase

#print(ascii_lowercase)

password = input("Ingrese la contraseña: ")

c = 0   #numero intentos
clave_des = ""

for i in password:   
    for j in ascii_lowercase:
        c = c+ 1
        if i == j:
            clave_des = clave_des + i
            break

print("La contraseña fue forzada en",c,"intentos")
print("La contraseña descifrada es:", clave_des)



""" 
i= primera letra de la contraseña
j = primera letra del abecedario ascii_lowercase(a a la z)
clave des = clave descifrada

clave des =  clave_des + i  para guardar la clave descifrada. primero clave des y despues +i, porque i es lo que se descubre. sino da la palabra al reves.
break para cortar/terminar el ciclo for

"""
