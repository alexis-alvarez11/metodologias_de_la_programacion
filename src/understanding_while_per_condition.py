"""Realizar un programa que defina un PIN como contraseña.
 
Despues vamos a darle 3 intentos al usuario para escriir el pin.

Si el usuario escribe correctamente el pin, el programa
debe mostrar un mensaje de Acceso Permitido

Si el usuario se equivoca, el programa debe decirle cuantos
intentis le quedan y en caso de que no queden intentos
el mensaje diga Acceso Denegado, excediste los intentos.

"""

CORRECT_PIN= "1234"
MAX_ATTEMTS= 3
intents= 0

while intents < MAX_ATTEMTS:

    user_pin= input("Escribe tu PIN: ")
    if user_pin == CORRECT_PIN:
        print("Acceso Permitido")
        break
    
    else: 
        intents +=1
        remaining_attemps= MAX_ATTEMTS - intents
        if remaining_attemps >0:
            print(f"PIN INCORRECTO, te quedan {remaining_attemps} intentos")
        else: 
            print("Acceso Denegado")



