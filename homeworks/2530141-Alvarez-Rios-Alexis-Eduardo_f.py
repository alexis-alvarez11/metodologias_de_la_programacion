
"***********************" 
"**FIBONACCI SERIES WITH PYTHON**"

"Alumno: ALEXIS EDUARDO ALVAREZ RIOS " 
"Matricula: 2530141  Grupo: 1-2"
"***********************" 

"""
URL: https://github.com/alexis-alvarez11/metodologias_de_la_programacion.git
"""


"""
RESUMEN EJECUTIVO:

La serie de Fibonacci es una sucesión de números donde cada número es la suma
 de los dos anteriores, empezando típicamente con 0 y 1.
Calcular la serie hasta n términos significa generar los primeros n números de 
la sucesión.
Cada término se obtiene sumando los dos anteriores de forma iterativa o recursiva.
El programa leerá n desde el usuario, validará que sea un entero positivo y 
generará la serie correspondiente.
Cubrirá la entrada de n, las validaciones básicas y la impresión de los términos 
de la serie.
"""


"""
Problem 7: Fibonacci Series Generation

Description:
El programa genera la serie de Fibonacci hasta n términos ingresados por el usuario. 
Comienza en 0 y 1 y muestra la sucesión completa en una línea.
    Inputs:
- n (int; número de términos a generar)
puts:
- Fibonacci series: <term_1> <term_2> ... <term_n>
    Validations:
- n entero
- n >= 1 y n <= 50
- Si falla la validación, mostrar "Error: invalid input"
    Test cases:
1) Normal: n=5 → 0 1 1 2 3
2) Border: n=1 → 0
3) Error: n=0 → Error
"""

# PROBLEM 
def fibonacci_series(n):
    """
    Devuelve una lista con los primeros n términos de la serie de Fibonacci.
    Parámetros:
        n (int): número de términos a generar (n >= 1)
    Retorna:
        list: serie de Fibonacci con n elementos
    """
    series = []
    f1, f2 = 0, 1
    if n >= 1:
        series.append(f1)
    if n >= 2:
        series.append(f2)
    for _ in range(3, n + 1):
        fn = f1 + f2
        series.append(fn)
        f1, f2 = f2, fn
    return series

try:
    n = int(input("Enter the number of terms: "))
except ValueError:
    print("Error: invalid input")
    exit()

if n < 1 or n > 50:
    print("Error: invalid input")
    exit()

fib_series = fibonacci_series(n)

print("Fibonacci series:", ' '.join(str(num) for num in fib_series))


"""
Reflexión:
Usar un bucle permitió generar la serie de Fibonacci de manera ordenada y eficiente 
para cualquier n.
Manejar los casos especiales n=1 y n=2 es importante para no generar errores ni 
duplicar valores.
Esta lógica se puede reutilizar en programas que requieran secuencias, cálculos o
simulaciones basadas en Fibonacci.


 Referencias:
1) Python documentation for and while loops
   https://docs.python.org/3/tutorial/controlflow.html#for-statements
 2) W3Schools Python Fibonacci Series
    https://www.w3schools.com/python/python_lists_comprehension.asp
 3) Real Python Fibonacci Series in Python
    https://realpython.com/python-fibonacci/
"""
