"""
if= si
else= no

== : comparación de igualdad en ambos lados
"""

cars= ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car== 'bmw':
        print(car.upper())
    else: 
        print(car)

# El condicional es el corazon de un if
# condicional True
car= 'bmw'
print(car== 'bmw')# true

#condicional False
car= 'Audi'
print(car== 'audi')

# Posible solucion a entrada del usuario
car= 'Audi'
print(car.lower()== 'audi') #True

#operador relacional != determina desigualdad
requested_topping= 'mushrooms'
if requested_topping != "anchovies": #True
    print("Hold the anchovies!")


# comparaciones numericas
age= 18 # entero
print(age == 18) #True

answer = 17
if answer != 42: #True
    print("Respuesta incorecta, intenta de nuevo!")

age= 20
print(age < 21) #True
print(age <= 21) #True
print(age> 21) #False
print(age >= 21) #False

# Mutiples condiciones
age_0= 22
age_1= 18
print(age_0 >= 21 and age_1 >= 21) # False (una o ambas falsas)
print(age_0 >= 21 or age_1 >= 18) #True

# Operacion or
print(age_0 >= 21 or age_1 >= 21) # True
print(age_0 >= 23 or age_1 >= 21) # False 

"""
Para preguntarnos si un valor especifico 
esta en una lista, podemos utilizar el sig. comparador:

Value in list
"""

motorcycles= ['mortaliza', 'honda', 'vento', 'yamaha']
moto_alex_wants= 'italika'
print(moto_alex_wants in motorcycles) #False
print('honda' in motorcycles) #True

"""
Para preguntarnos si un valor especifico 
 NO esta en una lista, podemos utilizar el sig. comparador:

Value not in list
"""
banned_students= ['jorge', 'carlos', 'moyra', 'gus', 'hots']
user= 'mauro'
print(user not in banned_students) #True
print('jorge' not in banned_students) #False


# Variables  del tipo booleano
game_active= True
can_edit= False


"""
    if statement

    sintasix: 

    if condition: 
        do something
    
    if condition:
        do something
    else:
        do something
"""


age= input("\n ¿Dime cual es tu edad?")
print(age)

if int(age)>= 18:
    print("Tienes edad para votar")
else:
    print("Eres menor de edad")