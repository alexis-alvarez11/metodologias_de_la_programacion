

"***********************" 
"** MANEJO DE FUNCIONES DE PYTHON ** Alumno: ALEXIS EDUARDO ALVAREZ RIOS " 
"Matricula: 2530141  Grupo: 1-2"

"""
URL: https://github.com/alexis-alvarez11/metodologias_de_la_programacion.git
"""


"""
RESUMEN EJECUTIVO:

 Una función en Python es un bloque de código que realiza una tarea específica 
y se puede reutilizar.
 Los parámetros son variables definidas en la función; los argumentos son los 
 valores que se pasan al llamarla.
 Separar la lógica en funciones reutilizables permite mantener el código más 
 organizado y fácil de mantener.
 Un valor de retorno es el resultado que la función entrega; devolver resultados 
 permite usarlos en otros cálculos o decisiones.
 Imprimir directamente limita la reutilización del resultado.
 Este documento cubrirá:
 - Descripción de cada problema
 - Diseño y documentación de funciones
 - Entradas y salidas esperadas
 - Validaciones de datos
 - Pruebas básicas con casos normales, bordes y de error
"""

# --------------------------------------------------
# PRINCIPIOS Y BUENAS PRÁCTICAS
# --------------------------------------------------
# - calculate_area y calculate_perimeter hacen solo su cálculo.
# - Funciones puras: devuelven valores sin imprimir.

"""
Problem 1: Rectangle Area and Perimeter

    Description:
El programa lee el ancho y alto de un rectángulo, valida que sean positivos 
y calcula su área y perímetro usando funciones.
    Inputs:
- width (float)
- height (float)
    Outputs:
- Area
- Perimeter
    Validations:
- width > 0
- height > 0
- Número válido
    Test cases:
1) Normal: width=4, height=5 → Area=20, Perimeter=18
2) Border: width=0.1, height=0.1 → Area=0.01, Perimeter=0.2
3) Error: width=-1, height=3 → Error
"""

# PROBLEM 1
def calculate_area(width, height):
    area= width * height
    return area

def calculate_perimeter(width, height):
    perimeter= 2 * (width + height)
    return perimeter

try:
    width= float(input("Enter width of rectangle: "))
    height= float(input("Enter height of rectangle: "))
except ValueError:
    print("Enter valid numbers")
    exit()

if width <= 0 or height <= 0:
    print("Error: Invalid input")
    exit()

area= calculate_area(width, height)
perimeter= calculate_perimeter(width, height)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

print("\n")


# --------------------------------------------------
# PRINCIPIOS Y BUENAS PRÁCTICAS
# --------------------------------------------------
# - classify_grade devuelve la letra de calificación según score.
# - Función pura: mismo score → mismo resultado.

"""
Problem 2: Grade Classification

Description:
El programa lee una calificación numérica, valida su rango y asigna una letra 
correspondiente (A-F).
    Inputs:
- score (float)
    Outputs:
- Letter grade (A, B, C, D, F)
    Validations:
- score numérico
- 0 <= score <= 100
    Test cases:
1) Normal: score=85 → Grade=B
2) Border: score=90 → Grade=A
3) Error: score=120 → Error
"""

# PROBLEM 2
def classify_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else: 
        return "F"
    
try:
    score= float(input("Enter your score: "))
except ValueError:
    print("Enter a valid number")
    exit()

if score < 0 or score > 100:
    print("Error: Invalid input")
    exit()

grade= classify_grade(score)
print(f"Your score is {score}")
print(f"Your grade is {grade}")

print("\n")


# --------------------------------------------------
# PRINCIPIOS Y BUENAS PRÁCTICAS
# --------------------------------------------------
# - summarize_numbers calcula min, max y average de la lista.
# - Función pura: no modifica la lista original.

"""
Problem 3: Number Summary

Description:
El programa recibe una lista de números separados por comas, la convierte a floats y
calcula el mínimo, máximo y promedio.
    Inputs:
- numbers_text (string)
    Outputs:
- Min, Max, Average
    Validations:
- Texto no vacío
- Conversión numérica válida
- Lista no vacía
    Test cases:
1) Normal: "10,20,30" → Min=10, Max=30, Avg=20
2) Border: "5" → Min=5, Max=5, Avg=5
3) Error: "a,10" → Error
"""

# PROBLEM 3
def summarize_numbers(numbers_list):
    summary = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return summary

numbers_text = input("Enter numbers separated by commas: ")

if not numbers_text.strip():
    print("Error: invalid input")
    exit()

try:
    numbers_list = [float(num.strip()) for num in numbers_text.split(",")]
except ValueError:
    print("Error: invalid input")
    exit()

if not numbers_list:
    print("Error: invalid input")
    exit()

summary = summarize_numbers(numbers_list)

print(f"Min: {summary['min']}")
print(f"Max: {summary['max']}")
print(f"Average: {summary['average']}")

print("\n")



# --------------------------------------------------
# PRINCIPIOS Y BUENAS PRÁCTICAS
# --------------------------------------------------
# - apply_discount genera una nueva lista con precios descontados.
# - Función pura: no altera la lista original.

"""
Problem 4: Apply Discount to Prices

Description:
El programa recibe precios separados por comas, valida que sean positivos 
y aplica un descuento para generar una nueva lista.
    Inputs:
- prices_text (string)
- discount_rate (float)
    Outputs:
- Original prices
- Discounted prices
    Validations:
- Texto no vacío
- Conversión a float válida
- Precios > 0
- 0 <= discount_rate <= 1
    Test cases:
1) Normal: "100,200", rate=0.1 → [100,200] → [90,180]
2) Border: "50", rate=1 → [50] → [0]
3) Error: "10,-5" → Error
"""

# PROBLEM 4
def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        discounted.append(new_price)
    return discounted

prices_text = input("Enter prices separated by commas: ")

if not prices_text.strip():
    print("Error: invalid input")
    exit()

try:
    prices_list = [float(p.strip()) for p in prices_text.split(",")]
except ValueError:
    print("Error: invalid input")
    exit()

if not prices_list:
    print("Error: invalid input")
    exit()

for price in prices_list:
    if price <= 0:
        print("Error: invalid input")
        exit()

try:
    discount_rate = float(input("Enter discount rate (0 to 1): "))
except ValueError:
    print("Error: invalid input")
    exit()

if discount_rate < 0 or discount_rate > 1:
    print("Error: invalid input")
    exit()

discounted_list = apply_discount(prices_list, discount_rate)

print("Original prices:", prices_list)
print("Discounted prices:", discounted_list)

print("\n")



# --------------------------------------------------
# PRINCIPIOS Y BUENAS PRÁCTICAS
# --------------------------------------------------
# - greet imprime un saludo, opcionalmente con título.
# - Documenta parámetros: name y title opcional.

"""
Problem 5: Greeting with Optional Title
    Description:
El programa pide un nombre y opcionalmente un título, y muestra un 
saludo personalizado usando una función con parámetro opcional.
    Inputs:
- name (string)
- title (string, opcional)
    Outputs:
- Greeting message
    Validations:
- name no vacío
    Test cases:
1) Normal: name="Alex", title="Dr" → "Hello, Dr Alex!"
2) Border: name="Ana", title="" → "Hello, Ana!"
3) Error: name="" → Error (no saludo)
"""

# PROBLEM 5
def greet(name, title=""):
    if title:
        print(f"Hello, {title} {name}!")
    else:
        print(f"Hello, {name}!")

try:
    name= input("Enter your name: ").strip().title()
    title_user= input("Enter your title (optional): ").strip().title()
    if title_user:
        greet(name, title_user)
    else:
        greet(name)
except ValueError:
    print("Error: invalid input")
    exit()

print("\n")



# --------------------------------------------------
# PRINCIPIOS Y BUENAS PRÁCTICAS
# --------------------------------------------------
# - factorial calcula n! usando un ciclo.
# - Función pura: mismo n → mismo resultado.

"""
Problem 6: Factorial Calculation

Description:
El programa lee un número entero no negativo, valida su 
rango y calcula su factorial usando un ciclo iterativo.
    Inputs:
- n (int)
    Outputs:
- n
- Factorial(n)
    Validations:
- n entero
- 0 <= n <= 20
    Test cases:
1) Normal: n=5 → 120
2) Border: n=0 → 1
3) Error: n=-3 → Error
"""

# PROBLEM 6
"""
Implementación usando método iterativo
Es más fácil de entender y seguir paso a paso.
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    n = int(input("Enter a non-negative integer: "))
except ValueError:
    print("Error: invalid input")
    exit()

if n < 0:
    print("Error: invalid input")
    exit()

if n > 20:
    print("Error: invalid input")
    exit()

fact_value = factorial(n)

print("n:", n)
print("Factorial:", fact_value)


"""
Las funciones permiten organizar el código en bloques claros y reutilizables, 
facilitando su mantenimiento.
Devolver valores con return es más flexible que imprimir, porque los resultados
se pueden usar en otros cálculos o decisiones.
Los parámetros y valores por defecto hacen que una función pueda trabajar con 
distintos datos sin cambiar su código.
Aprendí que la lógica principal debe ser clara y sencilla.
Esto hace que el programa sea más legible y fácil.
Además, facilita la reutilización de funciones en futuros proyectos.
"""


"""
# Referencias:
# 1) Python documentation Defining Functions (def, return, parameters)
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 2) W3Schools Python Functions Tutorial
#    https://www.w3schools.com/python/python_functions.asp
# 3) Real Python Defining Your Own Python Function
#    https://realpython.com/defining-your-own-python-function/
# 4) Libro: “Python Programming: An Introduction to Computer Science”, John Zelle
# 5) Artículo: “Best Practices for Writing Python Functions”, GeeksforGeeks
#    https://www.geeksforgeeks.org/best-practices-for-writing-python-functions/
"""
