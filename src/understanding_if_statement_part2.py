"""
Vamos a realizar un programa que pregunte ql usuario por su edad y 
muestre un mensaje diferente segun el rango de edad en el que 
se encuentre:
"""
# 1ra version
try:
    age= int(input("Introduce tu edad: "))

    if age >= 18:
        print("Eres mayor de edad")
    elif age < 18:
        print("Eres menor de edad")

except:
    print("Tuviste error al ingresar edad")

print("Hola Alexis")


# 2da version

try:
    age= int(input("Introduce tu edad: "))

except:
    age= -1
    print("Tuviste error al ingresar edad, no valido")

if age > 100:
        print("Estas muy old")
elif age >= 18 and age <= 100:
        print("Eres mayor de edad")
elif age < 18 and age >= 0:
        print("Eres menor de edad")
elif age < 0:     # else  (opcional, pero solo else, sino cumple nada de arriba)
        print("Tuviste un error")
print("Hola Alexis")


"""
hacer programa que pregunte edad y responda:

    -si edad es menor e igual a 4 entonces entrada gratuita
    -si la edad es menor e igual a 18, pero mayor que 4 entonces
    entrada cuesta $200
    -si la edad es mayor que 18, entonces la entrada cuesta $400
"""

#multiple if
guisos= ['desebrada', 'asado', 'salsa verde', 'pozole']
if 'asado' in guisos:
    print("Si hay asado")
else: 
    print("No hay asado")
if 'tamales'  in guisos:
    print("Si hay tamales")
else: 
    print("No hay tamales")
if 'salsa verde' in guisos:
    print("Si hay salsa verde")
else: 
    print("No hay salsa verde")
