"""

Un string es de manera sencilla una serie de caracteres
En Pygn todo lo que se encuentre dentro de comillas smples
'' o dobles comillas "" es considerado un string. 

"Esto es un string"
'Esto tambien es un string'

'Le dije a un amigo, "Pyton es mi lenguaje favorito!"'
"El lenguaje 'Python' lleva el nombre por Monty Python,
no por la serpiente" 

"POO= programacion orientada a objeto- metodos-atributos (unidad abstracta con metodos y atributos)"
"metodo-title: cambia la variable, pero no la modifica


"""

name= "clase de programacion " 
print(name)
print(name.title())
print(name)


"""
UN metodo es una accion que Python que puede realizar en un fragmento de datos o sobre una variable.

El punto . despues de un variable seguida del metodo title() dice que se tiene que ejecutar 
el metodo title() de la variable name.

Todos los metodos va seguidos de parentesis porque aveces necesitan informacion adicional 
para funciona, lo cual iria dentro de los parentesis.
En esta ocasion el metodo .title() no requiere informacion
para ejecutarse.


"""

print(name.upper())
print(name.lower())


# Concatenacion de STRINGS
print("CONCATENACION DE STRINGS")
first_name= "alexis"
last_name= "rios"
full_name= first_name +" "+ last_name
print(full_name)

print("Hola, " + full_name.title() + "!")


