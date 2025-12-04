
"***********************" 
"** MANEJO DE BUCLES DE PYTHON ** Alumno: ALEXIS EDUARDO ALVAREZ RIOS " 
"Matricula: 2530141  Grupo: 1-2"

"""
URL:
"""


"""
RESUMEN EJECUTIVO:

1. ¿Qué es un bucle for y para qué se usa típicamente?

Es una estructura de control que repite un bloque de código un número
 determinado de veces. Se usa típicamente cuando sabes de antemano cuántas veces
 quieres que se repita algo, como recorrer una lista, imprimir un patrón, o contar del 1
 al 10.

2. ¿Qué es un bucle while y cuándo es más natural usarlo?

Es una estructura de control que repite un bloque de código mientras se cumpla 
una condición. Es más natural usarlo cuando no sabes cuántas veces se repetirá la 
acción y depende de una condición que puede cambiar dentro del bucle.

3. ¿Qué son un contador y un acumulador?

Contador: Variable que se incrementa (o decrementa) para contar cuántas veces ocurre algo.
Ejemplo: contar cuántos números son pares en una lista.
Acumulador: Variable que suma o acumula valores para obtener un total.
Ejemplo: sumar todos los números de una lista.

4. ¿Por qué es importante definir bien la condición de salida y evitar ciclos infinitos?

Si la condición de salida no está bien definida, el bucle puede no terminar nunca, lo que
provoca que el programa se quede “pegado” o consuma recursos innecesarios.Definir 
correctamente cuándo detenerse asegura que el programa funcione de manera segura y 
eficiente.

5. ¿Qué cubrirá tu documento?

Este documento cubrirá ejemplos prácticos de uso de bucles for y while en Python,
incluyendo problemas como tablas de multiplicar, sumas acumuladoras, menus 
interactivos, etc.

"""

# ================================
# CONSEJOS DE BUCLES Y VARIABLES
# ================================
# - Usar for cuando conoces cuántas veces se repetirá (por ejemplo, del 1 al 10)
# - Usar while cuando la cantidad de repeticiones depende de una condición
#   (por ejemplo, leer hasta que el usuario escriba "EXIT")
# - Inicializar contadores y acumuladores antes del bucle
# - Actualizar variables de control dentro del while para evitar ciclos infinitos
# - Mantener el cuerpo del bucle simple; poner lógica compleja en funciones si es necesario

"""
Problem 1: Sumatoria y suma de pares
Description: Calcula la suma de todos los números desde 1 hasta un límite dado y, además, la suma de los números pares en ese rango.

Inputs:
num_n (int; número límite hasta el cual se sumarán los números).

Outputs:
Suma de todos los números del 1 a num_n.
Suma de todos los números pares del 1 a num_n.

Validations:
num_n debe ser un entero ≥ 1; si no, muestra “Error: invalid input”.

Test cases:
-Normal: num_n = 5 → Sum 1..5: 15, Even sum 1..5: 6
-Border: num_n = 1 → Sum 1..1: 1, Even sum 1..1: 0
-Error: num_n = 0 → Error: invalid input
    num_n = "abc" → Error: Invalid input

"""


# PROBLEM 1
try:
    num_n= int(input("Set your limit number: "))
except ValueError:
    print("Error: Invalid input")
    exit()

if num_n < 1:
    print("Error: invalid input")
    exit()

total_sum = 0
even_sum = 0

for i in range(1, num_n + 1):
    total_sum += i
    if i % 2 == 0:   
        even_sum += i

print(f"Sum 1..{num_n}: {total_sum}")
print(f"Even sum 1..{num_n}: {even_sum}")

print("\n")


"""
Problem 2: Tabla de multiplicar
Description: Imprime la tabla de multiplicar de un número hasta un límite dado.

Inputs:
base (int; número de la tabla)
m (int; límite de la tabla)

Outputs:
Cada línea de la tabla: base x i = resultado

Validations:
base y m deben ser enteros; m ≥ 1.

Test cases:
Normal: base = 3, m = 5 → 3x1=3 … 3x5=15
Border: base = 7, m = 1 → 7x1=7
Error: m = 0 → Error: Incorrect values
    base = "a" → Error: Invalid input

"""


# PROBLEM 2
try:
    base= int(input("Enter base: "))
    m= int(input("Enter limit of the table: "))
except ValueError:
    print("Error: Invalid input")
    exit()


if m < 1:
    print("Error: Incorrect values")
    exit()

for i in range(1, m + 1):
    product= base * i
    print(f"{base} x {i} = {product} ")

print("\n")


"""
Problem 3: Promedio con valor centinela
Description: Lee números del usuario hasta que se ingrese -1 y calcula el promedio y la cantidad de números ingresados.

Inputs:
Números (float; se ingresan uno por uno)

Outputs:
Cantidad de números ingresados
Promedio de los números

Validations:
Cada entrada debe ser un número; mostrar error si no lo es
Mostrar error si no se ingresó ningún número antes de -1

Test cases:
Normal: 5, 10, -1 → Count: 2, Average: 7.5
Border: -1 → Error: no data
Error: abc → Error: invalid input

"""


# PROBLEM 3
sentinel_value = -1

count = 0
total_sum = 0.0

while True:
    try:
        number = float(input("Enter a number (-1 to stop): "))
    except ValueError:
        print("Error: invalid input")
        continue  
    
    if number == sentinel_value:
        break

    total_sum += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average = total_sum / count
    print(f"Count: {count}")
    print(f"Average: {average}")

print("\n")

"""
Problem 4: Verificación de contraseña
Description: Permite ingresar una contraseña con un máximo de intentos.
Inputs: user_password (string)
 Outputs: Mensaje de acceso autorizado o denegado
 Validations: Máx. 3 intentos; comparar contra contraseña correcta
Test cases:
 1) Normal: "admin123" → Authorized Access
 2) Border: 3 intentos fallidos → Access Denied
 3) Error: cadenas distintas → Incorrect answer (hasta agotar intentos)

"""

# PROBLEM 4
CORRECT_PIN= "admin123"
MAX_ATTEMPTS= 3
attempts= 0

while attempts < MAX_ATTEMPTS:

    user_password= input("Enter your password: ")
    if user_password == CORRECT_PIN:
        print("Authorized Access ")
        break
    
    else: 
        attempts +=1
        remaining= MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"Incorrect answer, attempts: {remaining}")
        else: 
            print("Access Denied")

print("\n")

"""
Problem 5: Menú interactivo
Description: Muestra un menú con opciones para saludar, ver o incrementar un contador y salir.
Inputs: option (int; elección del usuario)
Outputs: Mensajes según la opción seleccionada
Validations: opción válida entre 0 y 3; mostrar error si no lo es
Test cases:
1) Normal: opción 1 → Hello!
2) Border: opción 0 → Bye!
3) Error: opción 5 o texto → Error: invalid option
"""

# PROBLEM 5
counter = 0

while True:
    print("\nMenu:")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_input = input("Select an option: ")

    try:
        option = int(option_input)
    except ValueError:
        print("Error: invalid option")
        continue

    if option == 0:
        print("Bye!")
        break

    elif option == 1:
        print("Hello!")

    elif option == 2:
        print(f"Counter: {counter}")

    elif option == 3:
        counter += 1
        print("Counter incremented")

    else:
        print("Error: invalid option")

print("\n")


"""
Problem 6: Triángulo de asteriscos
Description: Imprime un triángulo rectángulo de asteriscos según el número de filas.
Inputs: n (int; número de filas)
Outputs: Patrón de asteriscos línea por línea
Validations: n ≥ 1 y debe ser un entero
Test cases:
1) Normal: n=4 → *, **, ***, ****
2) Border: n=1 → *
3) Error: n=0 o texto → Error: invalid input
"""

# PROBLEM 6
n_input = input("Enter file numbers: ")

if not n_input.isdigit() or int(n_input) < 1:
    print("Error: invalid input")
else:
    n = int(n_input)

    for i in range(1, n + 1):
        print("*" * i)


"""
Reflexión sobre bucles y patrones:

For y while tienen usos distintos: for se usa cuando conocemos cuántas veces repetir 
algo, mientras que while depende de una condición que puede cambiar. 
Los contadores y acumuladores me ayudaron a llevar el registro de repeticiones y a sumar 
valores dentro de los bucles. 
Un riesgo al usar while es crear ciclos infinitos si no se actualiza correctamente la 
condición de salida. 
Los menús interactivos y los intentos de contraseña son ejemplos clásicos de while, 
porque dependen de que el usuario decida cuándo salir. 
Con los bucles anidados aprendí a generar patrones como triángulos de asteriscos, 
combinando control de filas y columnas de manera eficiente.
"""

"""
Referencias:

- Python documentation. "for statements." https://docs.python.org/3/tutorial/controlflow.html#for-statements
- Python documentation. "while statements." https://docs.python.org/3/tutorial/controlflow.html#while-statements
- Wirth, Niklaus. "Algorithms + Data Structures = Programs." Prentice Hall, 1976.
- Real Python. "Python Loops: for and while." https://realpython.com/python-for-loop/
- Apuntes de clase de Programación Básica, Universidad [tu universidad], 2025.
"""
