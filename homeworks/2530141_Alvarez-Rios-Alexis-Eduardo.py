
"***********************" 
"** MANEJO DE LISTAS, TUPLAS Y DICCIONARIOS ** Alumno: ALEXIS EDUARDO ALVAREZ RIOS " 
"Matricula: 2530141  Grupo: 1-2"

"""
URL:
"""

"""
Tipos de datos compuestos en Python:

Una lista es una colección mutable de elementos que se pueden modificar, agregar 
o eliminar. 
Una tupla es similar a una lista pero inmutable; una vez creada no se puede cambiar. 
Un diccionario asocia claves únicas con valores, permitiendo acceso rápido a 
datos mediante la clave. 
La mutabilidad de las listas permite actualizar información, mientras que la 
inmutabilidad de las tuplas garantiza seguridad de los datos. 
En este documento se describen problemas usando listas, tuplas y diccionarios, 
con entradas, salidas, validaciones y ejemplos prácticos como catálogos, registros 
y estadísticas.
"""

# ================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ================================
# - Usar listas cuando necesites agregar o eliminar elementos con frecuencia
# - Usar tuplas para datos que no deben cambiar (por ejemplo, coordenadas, 
# fechas, configuraciones fijas)
# - Usar diccionarios cuando necesites buscar información por una clave 
# (por ejemplo, por nombre, id, código)
# - Evitar modificar una lista mientras la recorres con un for, a menos que 
# sepas exactamente lo que haces
# - Usar nombres de claves descriptivos en los diccionarios (por ejemplo, "name", 
# "age", "price")
# - Escribir código legible y mensajes claros para el usuario


"""
Problem 1: Gestión de lista de productos
Description: Permite crear una lista de productos, agregar uno nuevo y buscar 
un producto en la lista.
Inputs: initial_items_text (string), new_item (string), search_item (string)
Outputs: Lista de productos, cantidad total y booleano indicando si se encontró 
el producto
Validations: No vacío; eliminar espacios extra al separar por comas
Test cases:
1) Normal: "pan, leche", "huevos", "leche" → Items list: ['pan', 'leche', 'huevos'],
 Total:3, Found item: True
2) Border: "agua", "jugo", "agua" → Total:2, Found item: True
3) Error: "", " ", "" → Mensajes de error
"""


#PROBLEM 1
initial_items_text = input("Enter products (comma separated): ")

if not initial_items_text:
    print("Error: invalid input")
    exit()

items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]

new_item = input("Enter new item: ").strip()
if not new_item:
    print("Error: invalid input")
    exit()

items_list.append(new_item)

search_item = input("Enter item to search: ").strip()
if not search_item:
    print("Error: invalid input")
    exit()

is_in_list = search_item in items_list

print(f"Items list: {items_list}")
print(f"Total items: {len(items_list)}")
print(f"Found item: {is_in_list}")

print("\n")


"""
Problem 2: Cálculo de distancia y punto medio
Description: Calcula la distancia euclidiana y el punto medio entre dos puntos 
en un plano 2D.
Inputs: x1, y1, x2, y2 (float)
Outputs: Punto A, Punto B, distancia y punto medio
Validations: Valores numéricos válidos
Test cases:
1) Normal: 0,0,3,4 → Distance: 5.0, Midpoint: (1.5, 2.0)
2) Border: 1,1,1,1 → Distance: 0.0, Midpoint: (1.0, 1.0)
3) Error: "a", 0 → Error: invalid input
"""


# PROBLEM 2
try:
    x1= float(input("Enter x1: "))
    y1= float(input("Enter y1: "))
    x2= float(input("Enter x2: "))
    y2= float(input("Enter y2: "))
except ValueError: 
   print("Error: invalid input")
   exit()

point_A= (x1, y1)
point_B= (x2, y2)

distance= ((x2 - x1)**2 + (y2 - y1)**2)**0.5
medium_point= ((x1 + x2)/2, (y1 + y2)/2)

print(f"Point A: {point_A}")
print(f"Point B: {point_B}")
print(f"Distance: {distance}")
print(f"Midpoint: {medium_point}")

print("\n")


"""
Problem 3: Cálculo de total de compra usando diccionario
Description: Calcula el total a pagar por un producto dado su precio unitario y cantidad usando un diccionario.
Inputs: product_name (string), quantity (int)
Outputs: Precio unitario, cantidad y total a pagar
Validations: Producto existente en el diccionario, cantidad >0, valores válidos
Test cases:
1) Normal: "apple", 3 → Unit price: 10.5, Quantity: 3, Total: 31.5
2) Border: "banana", 1 → Total: 8.9
3) Error: "", 0, "pear" → Mensajes de error
"""


#PROBLEM 3
product_prices= {"apple": 10.50, "banana": 8.90, "orange": 12.00, "grape": 15.75
                , "mango": 20.00}

try:
    product_name= input("Enter product name: ").strip().lower()
    quantity= int(input("Enter quantity: "))
except ValueError:
    print("Error invalid input")
    exit()

if not product_name or quantity <= 0:
    print("Error: incorrect values")
    exit()

if product_name in product_prices:
    unit_price = product_prices[product_name]
    total= unit_price * quantity
    print(f"Unit price: {unit_price}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total}")
else:
    print("Error: product not found")

print("\n")


"""
Problem 4: Promedio y aprobación de estudiante
Description: Calcula el promedio de calificaciones de un estudiante y determina si aprobó.
Inputs: student_name (string)
Outputs: Lista de calificaciones, promedio y booleano indicando aprobación (>=70)
Validations: Nombre no vacío y estudiante existente
Test cases:
1) Normal: "Alice" → Grades: [90,85,100], Average: 91.67, Passed: True
2) Border: "Diana" → Average: 81.67, Passed: True
3) Error: "", "Bob" → Mensajes de error
"""


# PROBLEM 4
students= {
    "Alice": [90, 85, 100],
    "Jorge": [78, 82, 95],
    "Charlie": [100, 100, 100],
    "Diana": [80, 75, 90],
    "Alexa": [90, 95, 100]
           }

try:
    student_name= input("Name of the student: ").strip().title()
    if not student_name:
        print("Error: invalid input")
        exit()
except ValueError:
    print("Error: incorrect values")
    exit()

if student_name in students:
    grades= students[student_name]
    average= sum(grades) / len(grades)
    print(f"Grades: {grades}")
    print(f"Average: {average}")
    if average >= 70:
        print("Passed: True")
    else:
        print("Passed: False")
else:
    print("Error: student not found")

print("\n")


"""
Problem 5: Frecuencia de palabras en una oración
Description: Analiza una oración, cuenta la frecuencia de cada palabra y determina 
la más común.
Inputs: sentence (string)
Outputs: Lista de palabras, diccionario de frecuencias y palabra más común
Validations: No vacío; eliminar signos de puntuación y normalizar a minúsculas
Test cases:
1) Normal: "Hola mundo hola" → Words list: ['hola','mundo','hola'], Frequencies: 
{'hola':2,'mundo':1}, Most common word: 'hola'
2) Border: "Python" → Most common word: 'python'
3) Error: "" → Error: Invalid input
"""


# PROBLEM 5
sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("Error: Invalid input")
    exit()

for p in [".", ",", "!", "?"]:
    sentence = sentence.replace(p, " ")

words_list = sentence.lower().split()

if not words_list:
    print("Error: words not found")
    exit()

freq_dict = {}

for word in words_list:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

most_common_word = None
max_freq = 0

for word, freq in freq_dict.items():
    if freq > max_freq:
        max_freq = freq
        most_common_word = word

print("Words list:", words_list)
print("Frequencies:", freq_dict)
print("Most common word:", most_common_word)

print("\n")


"""
Problem 6: Gestión de contactos
Description: Permite agregar, buscar o eliminar contactos usando un diccionario.
Inputs: action_text (ADD/SEARCH/DELETE), name (string), phone (string para ADD)
Outputs: Mensajes confirmando acción y datos de contacto
Validations: Acción válida, campos no vacíos, contacto existente para SEARCH/DELETE
Test cases:
1) Normal: ADD "Ana", "12345" → Contact saved: Ana 12345
2) Border: SEARCH "Carlos" → Phone: 8341142724
3) Error: DELETE "Bob" → Error: contact not found
"""


# PROBLEM 6
contacts = {
    "Alexa": "8341151925",
    "Jorge": "8321075842",
    "Carlos": "8341142724"
}

action_text = input("Acción (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
    exit()

if action_text == "ADD":
    name = input("Name of the contact: ").strip().title()
    phone = input("Telephone number: ").strip()

    if not name:
        print("Error: name cannot be empty")
        exit()
    if not phone:
        print("Error: phone cannot be empty")
        exit()

    contacts[name] = phone
    print("Contact saved:", name, phone)

elif action_text == "SEARCH":
    name = input("Name of the contact: ").strip().title()

    if not name:
        print("Error: name cannot be empty")
        exit()

    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Error: contact not found")

elif action_text == "DELETE":
    name = input("Name of the contact: ").strip().title()

    if not name:
        print("Error: name cannot be empty ")
        exit()

    if name in contacts:
        contacts.pop(name)
        print("Contact deleted:", name)
    else:
        print("Error: contact not found")

print("\n")


"""
Reflexión sobre listas, tuplas y diccionarios:

Las listas son útiles cuando necesitamos modificar datos con frecuencia, agregando 
o eliminando elementos. 
Las tuplas son ideales para almacenar datos que no deben cambiar, como coordenadas
 o fechas. 
Los diccionarios permiten búsquedas rápidas mediante claves, facilitando el acceso
 a información específica. 
Combinar estas estructuras, como diccionarios que contienen listas, ayuda a organizar
 datos complejos de manera eficiente. 
Aprendí que elegir la estructura correcta depende de la necesidad de mutabilidad, 
rapidez de acceso y claridad del código.
"""


"""
Referencias:

- Python documentation. "Built-in Types: list, tuple, dict." https://docs.python.org/3/library/stdtypes.html
- Real Python. "Python Data Structures: Lists, Tuples, and Dictionaries." https://realpython.com/python-data-structures/
- Wirth, Niklaus. "Algorithms + Data Structures = Programs." Prentice Hall, 1976.
- Tutorial de Python sobre estructuras de datos básicas, https://www.learnpython.org/
- Apuntes de clase de Programación Básica, Universidad [tu universidad], 2025.
"""
