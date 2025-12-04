"""
Docstring for understanding_while_loop

Utilizamos el whie para ejeccutar unbloque de codigo mientras 
una condicion sea verdadera.

Estrutura basica del while loop en Python:

        while condition:
            # Bloque de codigo a ejecutar

"""
# Ejemplo basico de un while loop
# Verificar si un numero esta en un 
# rango especifico (10 y entre 20)

while True: # while loop infinito
    try:
        number= int(input("Ingrese un numero entre 10 y 20: "))

        if number <20 and number >10:
            print("Numero dentro del rango")
            break
        else:
            print("Numero fuera del rango")
    except ValueError:
        print("Entrada invalida, ingresa entero")
    except KeyboardInterrupt:
        print("\nPrograma terminado por usuario")
        break