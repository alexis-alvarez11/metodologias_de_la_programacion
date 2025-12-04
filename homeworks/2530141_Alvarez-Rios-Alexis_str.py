"***********************" 
"** MANEJO DE STRINGS ** Alumno: ALEXIS EDUARDO ALVAREZ RIOS " 
"Matricula: 2530141  Grupo: 1-2"

"""
URL:
"""

"""
'¿Qué es un String?' "Un string, o cadena de texto, es un tipo de dato en programación" 
"que representa una secuencia de carácteres, como letras, números y símbolos, " 
"usualmente delimitada por comillas. Se utiliza para almacenar y manipular texto, " 
"como palabras, frases o datos alfanuméricos. " 

"¿Qué operaciones básicas se pueden realizar?" " "
"-Concatenación: Unir dos o más cadenas de texto. El operador + se usa comúnmente para esto. " 
"-Longitud: Obtener el número de caracteres que componen una cadena.  " 
"-Indexación: Acceder a caracteres individuales dentro de una cadena usando su posición
 (índice). "
"-Slicing: Extraer una subcadena de una cadena más grande usando rangos de índices. "
"-Búsqueda: Encontrar la posición de una subcadena dentro de una cadena. "
"-Reemplazo: Sustituir partes de una cadena por otras. "
"-Transformaciones: Convertir mayúsculas a minúsculas, eliminar espacios en blanco, etc. "

- ¿Por qué es importante validar y normalizar texto de entrada (por ejemplo, correos, nombres, contraseñas)?
Es importante validar y normalizar texto para asegurarse de que cumpla con el formato 
esperado, evitar errores, mejorar la consistencia de los datos y prevenir problemas de 
seguridad como inyecciones o entradas inválidas.

- ¿Qué cubrirá tu documento?
Este documento cubrirá ejemplos prácticos de manipulación de strings en Python,
    incluyendo validación de correos electrónicos, formateo de nombres, verificación de
    contraseñas, y análisis de texto.
"""

# ================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ================================
# - Los strings son inmutables: cualquier cambio genera una nueva cadena
# - Normalizar entradas con strip() y lower() antes de compararlas
# - Evitar "números mágicos" en índices; documentar qué extrae cada slice
# - Usar métodos de string en lugar de reescribir lógica básica
# - Diseñar validaciones claras: primero que no esté vacío, luego el formato
# - Escribir código legible: nombres de variables claros y mensajes de error entendibles


"""
Problem 1: Formateo de nombre completo
Description: Pide un nombre completo, lo formatea con mayúsculas iniciales y genera las iniciales.
Inputs: full_name (string)
Outputs: Nombre formateado y sus iniciales
Validations: No vacío, al menos nombre y apellido
Test cases:
1) Normal: "juan perez" → Formatted Name: Juan Perez, Initials: J.P.
2) Border: "Ana Lopez" → Formatted Name: Ana Lopez, Initials: A.L.
3) Error: "" → Error: Name cannot be empty; "Juan" → Error: Enter at least first name and last name
"""

" PROBLEM 1"

full_name= input("Enter your full name: ").strip()
words= full_name.split()
if not full_name:
    print("Error: Name cannot be empty")
elif len(words) <2: 
    print("Error: Enter at least first name and last name")
else:
    formatted_name= ' '.join(word.title() for word in words)
    initials=  '.'.join(word[0].upper() for word in words) + '.'

    print(f"Formatted Name: {formatted_name}")
    print(f"Initials: {initials}") 

print("\n")


"""
Problem 2: Validación de correo electrónico
Description: Verifica si un correo tiene formato básico válido y extrae el dominio.
Inputs: email (string)
Outputs: Indica si es válido y muestra el dominio
Validations: No vacío, sin espacios, exactamente un '@', dominio con '.'
Test cases:
1) Normal: "user@example.com" → Valid email: True, Domain: example.com
2) Border: "a@b.c" → Valid email: True, Domain: b.c
3) Error: "", "user@@example.com", "user example.com" → Mensajes de error
"""


"PROBLEM 2"

email= input("Enter your email address: ").strip()
if not email:
    print("Error: Invalid email adress")
elif ' ' in email:
    print("Error: Email cannot contain spaces")

sign= email.count('@')
if sign != 1:
    print("Invalid email")
    exit()

position= email.find('@')
domain= email[position +1:]
if '.' not in domain:
    print("Valid email: False")
else:
    print("Valid email: True")
    print(f"Domain: {domain}")

print("\n")


"""
Problem 3: Verificación de palíndromo
Description: Determina si una palabra o frase es un palíndromo ignorando mayúsculas y 
espacios.
Inputs: palindrome (string)
Outputs: Indica True si es palíndromo, False si no
Validations: No vacío
Test cases:
1) Normal: "Ana" → Is palindrome: True
2) Border: "a" → Is palindrome: True
3) Error: "" → Error: Input cannot be empty
"""


"PROBLEM 3"

palindrome= input("Enter word or phrase: ").strip()
if not palindrome:
    print("Error: Input cannot be empty")


normalized= palindrome.lower().replace(" ", "")
reversed_text= normalized[::-1]
if normalized == reversed_text:
    print("Is palindrome: True")
else:
    print("Is palindrome: False")

print("\n")


"""
Problem 4: Análisis de palabras en una oración
Description: Analiza una oración mostrando cantidad de palabras, primera, última, más 
corta y más larga.
Inputs: text (string)
Outputs: Cantidad de palabras, primera, última, más corta y más larga
Validations: No vacío, al menos dos palabras
Test cases:
1) Normal: "Hola mundo Python" → Text length:3, First: Hola, Last: Python, 
Shortest: Hola, Longest: Python
2) Border: "Hola mundo" → Text length:2, First: Hola, Last: mundo, Shortest: Hola, 
Longest: mundo
3) Error: "" → Error: Input cannot be empty; "Hola" → Error: Enter at least two words
"""

"PROBLEM 4"
text= input("Enter your sentence: ").strip().split()
if not text:
    print("Error: Input cannot be empty")
text_length= len(text)
if text_length <2:
    print("Error: Enter at least two words")
else:
    print(f"Text length: {text_length}")

    first_word= text[0]
    last_word= text[-1]
    shortest_word= min(text, key=len)
    longest_word= max(text, key=len)
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")
    
print("\n")


"""
Problem 5: Evaluación de fuerza de contraseña
Description: Clasifica la contraseña como débil, media o fuerte según su longitud y 
caracteres.
Inputs: password (string)
Outputs: Password strength: Weak, Medium o Strong
Validations: No vacío; mínimo 8 caracteres para fuerza
Test cases:
1) Normal: "Abc123!@" → Password strength: Strong
2) Border: "Abc12345" → Password strength: Medium
3) Error: "" → Error: Password cannot be empty
"""

"PROBLEM 5"
password= input("Enter you password: ").strip()
if not password: 
    print("Error: Password cannot be empty")
    exit()

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(not c.isalnum() for c in password)

if len(password) < 8:
    print("Password strength: Weak")
elif has_upper and has_lower and has_digit and has_symbol:
    print("Password strength: Strong")
else:
    print("Password strength: Medium")

print("\n")


"""
Problem 6: Generación de etiqueta de producto
Description: Crea una etiqueta con nombre y precio, ajustando su longitud a 30 caracteres.
Inputs: product_name (string), price_value (string/float)
Outputs: Label de 30 caracteres con nombre y precio
Validations: No vacío, precio válido y no negativo
Test cases:
1) Normal: "Lapicero", 2.5 → Label: 'Product: Lapicero|Price: $2.5      '
2) Border: "Libro", 12 → Label ajustado a 30 caracteres
3) Error: "", "-5", "abc" → Mensajes de error correspondientes
"""


"PROBLEM 6"
product_name = input("Enter your product name: ").strip()
price_value = input("Enter the price value: $").strip()

if not product_name or not price_value:
    print("Error: Input cannot be empty")
    exit()

try:
    price = float(price_value)
    if price < 0:
        print("Error: Price cannot be negative")
        exit()
except ValueError:
    print("Error: Price must be a valid number")
    exit()

label = f"Product: {product_name}|Price: ${price}"

if len(label) < 30:
    label = label + " " * (30 - len(label))
else:
    label = label[:30]

print(f"Label: '{label}'")

print("\n")


"""
Reflexión sobre manejo de strings:

El manejo de strings es esencial para procesar y mostrar datos correctamente. 
Métodos como lower(), strip(), split() y join() ayudan a normalizar, separar y unir 
texto de forma eficiente. 
Normalizar texto antes de compararlo evita errores por mayúsculas, espacios o formatos 
inconsistentes. 
Diseñar validaciones claras previene errores y garantiza que los datos sean confiables. 
Aprendí que los strings son inmutables, por lo que cualquier cambio crea una nueva 
cadena, y que los slices sirven paara extraer partes específicas.
"""


"""
Referencias:

- Python documentation. "Built-in Types: Text Sequence Type — str." https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
- Real Python. "Python Strings: Working with Text Data." https://realpython.com/python-strings/
- Wirth, Niklaus. "Algorithms + Data Structures = Programs." Prentice Hall, 1976.
- Tutorial de Python sobre validación de entradas y manejo de strings, https://www.learnpython.org/
- Clase de Programación Básica, Universidad, 2025.
"""
    


