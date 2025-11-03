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


#Syntax error con strings
message= "Una fortaleza de Python es su comunidad"
print(message)

message= "Una fortaleza de 'Python' es su comunidad"
print(message)


#Concatenacion con f-strings
famous_person= "Alexis Alvarez"
quote= "Python is love"

#Concatenacion convencional
message= famous_person +" una vez dijo "+ quote
print(message)

#Concatenacion con f-strings
message_f_strings= f"{famous_person} una vez dijo {quote}"
print(message_f_strings)

#Actividad

"""
1) Personaje famoso igualalo a variable string
2) Elige una frase famosa que haya dicho e igualalo a string
3) Genera un mensaje con las dos avariables utilizando f-string
4) Imprime el mensaje
"""

famous= "Oppen Heimer"
famous_phrase= "me he convertido en la muerte, el destructor de mundos"

message_heimer= f"{famous} una vez dijo, {famous_phrase}"
print(message_heimer)


#Whitespaces

"""
Whitespace se refiere a cualquier caracter que no se imprime, 
es decir, un tabulador y fines de linea. Los whitespaces se utilizan comunmente 
para organizar las salidas (prints)
de tal manera que sea mas amigable de leer o ver para los usuarios.
"""

#Ejemplos
print("Pyhon")
print("\tPython") #Tabulador
print("\t\tPython") #Tabulador

#Ejemplo de salto de linea
print("Languages: \n Python \n C \n Javascript")

#Eliminacion de espacios en blanco
programming_languages= " Python "
print(programming_languages)
print(programming_languages.lstrip())
print(programming_languages.rstrip())
print(programming_languages.strip())


