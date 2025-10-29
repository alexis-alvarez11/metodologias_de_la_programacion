message = "This is my first python variable"
another_message ='I am really, really really happy'

#print () -> use to show message in terminal
#print () -> se utiliza para mostrar mensajes en la terminal

print(message)
print(another_message)
print(message, another_message, message)
print(another_message, message)

message = "I love Python"
print(message)

alexis_message = "Hola soy alexis, y aprendo python"
print(alexis_message)

"""
Traceback: Es un registro donde el interprete tuvo problemas al intentar ejecutar su código.

Ejemplo: 
Traceback (most recent call last):
 File "C:/Users/Acer/Desktop/projects/metodologias_de_la_programacion/src/understanding_variables.py", line 17, in <module>
    print(alexis_mesage)
          ^^^^^^^^^^^^^
NameError: name 'alexis_mesage' is not defined. Did you mean: 'alexis_message'?

name error: significa que olvdamos establecer el valor de una variable antes de utilizar o 
cometimos un error al ingresar el nombre de la variable.


"""