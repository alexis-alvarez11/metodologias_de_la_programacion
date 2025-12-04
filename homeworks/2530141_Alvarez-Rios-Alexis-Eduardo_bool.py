
"***********************" 
"** MANEJO DE NUMEROS Y BOOLEANOS ** Alumno: ALEXIS EDUARDO ALVAREZ RIOS " 
"Matricula: 2530141  Grupo: 1-2"

"""
URL: https://github.com/alexis-alvarez11/metodologias_de_la_programacion.git
"""

"""
Tipos de datos en Python:

Los tipos int y float representan números enteros y números con decimales, 
respectivamente; se diferencian en que los float permiten fracciones mientras que los 
int no. 
Un booleano es un valor True o False que se obtiene al evaluar comparaciones o 
condiciones lógicas. 
Validar rangos y evitar divisiones entre cero es crucial para prevenir errores de 
ejecución y resultados inválidos. 
En este documento se describen los problemas resueltos, el diseño de entradas y salidas, 
las validaciones implementadas y cómo se usan enteros, flotantes y booleanos para controlar
la lógica y la toma de decisiones.
"""

# ================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ================================
# - Usar tipos apropiados: int para contadores, float para cantidades con decimales
# - Evitar duplicar expresiones complejas; guardar resultados intermedios en variables
# - Validar datos antes de operar (por ejemplo, que horas y salarios no sean negativos)
# - Usar nombres de variables descriptivos y mensajes claros para el usuario
# - Documentar claramente cómo se interpretan los booleanos (qué significa True y False
#  en cada contexto)


"""
Problem 1: Conversión de temperatura y detección de calor
Description: Convierte una temperatura en Celsius a Fahrenheit y Kelvin, e indica si es alta.
Inputs: temp_c_text (string convertible a float)
Outputs: Temperatura en °F y °K, booleano indicando si es alta (>=30°C)
Validations: No vacío, valor numérico válido, Kelvin ≥0
Test cases:
1) Normal: "25" → Farenheit: 77.0 °F, Kelvin: 298.15 °K, High temperature: False
2) Border: "30" → High temperature: True
3) Error: "", "abc", "-300" → Mensajes de error correspondientes
"""


# PROBLEM 1
temp_c_text= input("Enter celsius temperature: ").strip()
if not temp_c_text:
    print("Error: input cannot be empty")
    exit()
try:
    temp_c= float(temp_c_text)
except ValueError:
    print("Error: impossible temperature")
    exit()

temp_f= (temp_c *9/5 ) + 32
temp_k= temp_c + 273.15
if temp_k < 0.0:
    print("Error: impossible temperature (Kelvin < 0)")
    exit()

print(f"Farenheit: {temp_f} °F")
print(f"Kelvin: {temp_k} °K")
    
is_high_temperature = temp_c >= 30.0
if is_high_temperature:
    print("High temperature: True")
else:
    print("High temperature: False")

print("\n")


"""
Problem 2: Cálculo de salario con horas extra
Description: Calcula el pago regular y por horas extra según horas trabajadas y tarifa.
Inputs: hours_worked (float), hourly_rate (float)
Outputs: Pago regular, pago por horas extra, pago total, booleano indicando horas extra
Validations: No negativo, tarifa >0, valores numéricos
Test cases:
1) Normal: 45 h, $10 → Regular: 400, Overtime: 75, Total: 475, Has overtime: True
2) Border: 40 h, $12 → Has overtime: False
3) Error: -5, 0, "abc" → Mensajes de error
"""


# PROBLEM 2
try:
    hours_worked= float(input("Enter your hours worked: "))
    hourly_rate= float(input("Enter your hourly rate: "))
except ValueError:   
    print("Error: Set your correct values")
    exit()

if hours_worked < 0 or hourly_rate <= 0:
    print( "Error: invalid input")
    exit()

regular_hours = min(hours_worked, 40)
overtime_hours = max(hours_worked - 40, 0)

regular_pay= regular_hours * hourly_rate
overtime_pay= overtime_hours * hourly_rate * 1.5
total_pay= regular_pay + overtime_pay

if hours_worked > 40:
    print("Has overtime: True")
else: 
    print("Has overtime: False")

print(f"Regular pay: {regular_pay} ")
print(f"Overtime pay: {overtime_pay}")
print(f"Total pay: {total_pay}")

print("\n")


"""
Problem 3: Cálculo de descuento de compra
Description: Determina si un cliente es elegible para descuento y calcula el total final.
Inputs: purchase_total_user (float), is_student_user (YES/NO), is_senior_user (YES/NO)
Outputs: Booleano indicando elegibilidad y total final con descuento si aplica
Validations: Total ≥0, respuestas válidas YES/NO, valores numéricos correctos
Test cases:
1) Normal: 1200, YES, NO → Discount eligible: True, Final total: 1080.0
2) Border: 900, NO, NO → Discount eligible: False, Final total: 900.0
3) Error: -50, "maybe", "abc" → Mensajes de error
"""


# PROBLEM 3
try:
    purchase_total_user= float(input("Enter your total: "))
    is_student_user= input("Are you a student? YES/NO: ").strip().upper()
    is_senior_user= input("Are a you a senior? YES/NO: ").strip().upper()
except ValueError:
    print("Error: set correct values")
    exit()

if purchase_total_user < 0:
    print("Error: Set correct values")
    exit()

if is_student_user not in ("YES", "NO") or is_senior_user not in ("YES", "NO"):
    print("Error: Invalid input")
    exit()

is_student= is_student_user == "YES"
is_senior= is_senior_user == "YES"

discount_eligible= is_student or is_senior or purchase_total_user >= 1000

if discount_eligible:
    final_total= purchase_total_user * 0.9
else:
    final_total= purchase_total_user

print(f"Discount eligible: {discount_eligible} ")
print(f"Final total: {final_total}")

print("\n")


"""
Problem 4: Cálculo de descuento de compra
Description: Determina si un cliente aplica para descuento y calcula el total final.
Inputs: purchase_total_user (float), is_student_user (YES/NO), is_senior_user (YES/NO)
Outputs: Booleano indicando elegibilidad y total final con descuento si aplica
Validations: Total ≥0, respuestas YES/NO, valores numéricos correctos
Test cases:
1) Normal: 1200, YES, NO → Discount eligible: True, Final total: 1080.0
2) Border: 900, NO, NO → Discount eligible: False, Final total: 900.0
3) Error: -50, "maybe", "abc" → Mensajes de error
"""


# PROBLEM 4
try: 
    n_1= int(input("Enter number 1: "))
    n_2= int(input("Enter number 2: "))
    n_3= int(input("Enter number 3: "))
except ValueError:
    print("Error: incorrect values")

sum= n_1 + n_2 + n_3
average= float(sum) / 3
min_value= min(n_1, n_2, n_3)
max_value= max(n_1, n_2, n_3)

print(f"Sum: {sum}")
print(f"Average: {average}")
print(f"Min: {min_value}")
print(f"Max: {max_value}")

if (n_1 %2 ==0) and (n_2 %2 ==0) and (n_3 %2 ==0):
    print("All even: True")
else:
    print("All even: False")

print("\n")


"""
Problem 5: Elegibilidad de crédito
Description: Calcula la relación deuda-ingreso y determina si un cliente es elegible para crédito.
Inputs: monthly_income (float), monthly_debt (float), credit_score (int)
Outputs: Debt ratio y booleano indicando elegibilidad
Validations: Ingresos >0, deuda y puntaje ≥0, valores numéricos
Test cases:
1) Normal: 10000, 3000, 700 → Debt ratio: 0.3, Eligible: True
2) Border: 8000, 3200, 650 → Debt ratio: 0.4, Eligible: True
3) Error: -5000, -100, "abc" → Mensajes de error
"""


# PROBLEM 5
try:
    monthly_income= float(input("Enter your monthly income: "))
    monthly_debt= float(input("Enter your monthly debt: "))
    credit_score= int(input("Enter your credit score: "))
except ValueError:
    print("Error: Incorrect values")
    exit()

if (monthly_income <= 0) or (monthly_debt < 0) or (credit_score < 0):
    print("Error: invalid input")
    exit()

debt_ratio = monthly_debt / monthly_income
eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)

print(f"Debt ratio: {round(debt_ratio,2)}")
if eligible:
    print("Eligible: True")
else:
    print("Eligible: False")

print("\n")


"""
Problem 6: Cálculo de IMC
Description: Calcula el índice de masa corporal (IMC) y clasifica al usuario como bajo peso, normal o sobrepeso.
Inputs: weight_kg (float), height_m (float)
Outputs: BMI y booleanos indicando categoría (Underweight, Normal, Overweight)
Validations: Peso y altura >0, valores numéricos
Test cases:
1) Normal: 70, 1.75 → BMI: 22.86, Underweight: False, Normal: True, Overweight: False
2) Border: 60, 1.75 → BMI: 19.59, Normal: True
3) Error: -70, 0, "abc" → Mensajes de error
"""


# PROBLEM 6
try: 
    weight_kg= float(input("Enter your weight: "))
    height_m= float(input("Enter your height: "))
except ValueError:
    print("Error: incorrect values")
    exit()

if weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input")
    exit()

bmi = float(weight_kg / (height_m * height_m))
bmi= round(bmi, 2)

is_underweight= (bmi < 18.5)
is_normal= (18.5 <= bmi and bmi < 25.0)
is_overweight= (bmi >= 25.0)

print(f"BMI: {bmi}")

if is_underweight:
    print("Underweight: True")
else:
    print("Underweight: False")
if is_normal:
    print("Normal: True")
else:
    print("Normal: False")
if is_overweight:
    print("Overweight: True")
else:
    print("Overweight: False")


"""
Reflexión sobre enteros, flotantes y booleanos:

Los enteros y flotantes se usan juntos para realizar cálculos precisos, como salarios, IMC o conversiones de temperatura. 
Las comparaciones generan booleanos que permiten tomar decisiones mediante estructuras if. 
Validar rangos y evitar divisiones entre cero previene errores y resultados inválidos. 
Aprendí a combinar condiciones con and, or y not para controlar flujos complejos de manera clara. 
Estos patrones se repiten en problemas de nómina, descuentos, elegibilidad de préstamos y cálculos financieros en general.
"""


"""
Referencias:

- Python documentation. "Built-in Types: Numeric Types — int, float, complex." https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
- Python documentation. "Boolean type — bool." https://docs.python.org/3/library/stdtypes.html#boolean-values
- Real Python. "Python Operators: Arithmetic, Comparison, and Logical Operators." https://realpython.com/python-operators-expressions/
- Wirth, Niklaus. "Algorithms + Data Structures = Programs." Prentice Hall, 1976.
- Apuntes de clase de Programación Básica, Universidad [tu universidad], 2025.
"""

