"***********************" 
"**    CRUD    **"

"Alumno: ALEXIS EDUARDO ALVAREZ RIOS " 
"Matricula: 2530141  Grupo: 1-2"
"***********************" 

"""
URL: https://github.com/alexis-alvarez11/metodologias_de_la_programacion.git
"""

"""
Resumen Ejecutivo:
--------------------------------------------------
Implementa un CRUD (Create, Read, Update, Delete) en memoria 
utilizando un diccionario de diccionarios para manejar items de inventario.
Cada operación (create, read, update, delete, list) está en su propia 
función.
El programa ofrece un menú interactivo para que el usuario elija la operación a 
realizar.
Se validan entradas, controlan duplicados y se muestran mensajes claros del 
resultado.
El código es, reutilizable y fácilmente extensible a sistemas más grandes.
"""

# --------------------------------------------------
# Descripción 
# --------------------------------------------------
# Programa que implementa un CRUD simple para elementos de inventario en 
# memoria usando un diccionario de diccionarios.
# Cada operación (Crear, Leer, Actualizar, Eliminar, Listar) está en su propia 
# función, y el usuario interactúa mediante un menú de texto.
# Se validan las entradas y se muestran mensajes claros de resultado.


"""
--------------------------------------------------
Problem: CRUD con funciones
--------------------------------------------------
 Descripción:
Programa que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) simple para elementos almacenados en un diccionario,
usando funciones para cada operación y un menú de texto para interactuar con el usuario.

Inputs:
- Opciones del menú (string o int)
- Para CREAR/ACTUALIZAR: item_id, name, price, quantity (o los campos que definas)
- Para LEER/ELIMINAR: item_id

Outputs:
- Mensajes indicando el resultado de cada operación:
 - "Item created", "Item updated", "Item deleted", "Item not found", "Items list:", etc.

# Validations:
# - La opción del menú debe ser válida (por ejemplo, 0..5 según tu diseño)
# - item_id no debe estar vacío
# - Los campos numéricos deben ser números válidos y mayores o iguales a 0
# - No se permite crear un item con un id ya existente (documenta tu decisión)
# - Para LEER/ACTUALIZAR/ELIMINAR, si el id no existe, mostrar "Item not found"

# Test cases:
# 1) Normal: crear un item, leerlo, actualizarlo, eliminarlo → mensajes esperados y estado final correcto
# 2) Borde: intentar crear un item con datos mínimos válidos (por ejemplo, quantity=0) o usar un id muy corto/largo
# 3) Error: usar opción de menú inválida, id vacío, precio o cantidad no numérica → mostrar mensajes de error

"""
# PROBLEM
items = {}

def create_item(items_dict, item_id, name, price, quantity):
    """Creates a new item in the dictionary. Returns True if created, False if id exists."""
    if item_id in items_dict:
        return False
    items_dict[item_id] = {"name": name, "price": price, "quantity": quantity}
    return True

def read_item(items_dict, item_id):
    """Returns the item dict if found, None otherwise."""
    return items_dict.get(item_id)

def update_item(items_dict, item_id, name, price, quantity):
    """Updates an existing item. Returns True if updated, False if not found."""
    if item_id not in items_dict:
        return False
    items_dict[item_id] = {"name": name, "price": price, "quantity": quantity}
    return True

def delete_item(items_dict, item_id):
    """Deletes an item. Returns True if deleted, False if not found."""
    if item_id not in items_dict:
        return False
    del items_dict[item_id]
    return True

def list_items(items_dict):
    """Prints all items in a readable format."""
    if not items_dict:
        print("Items list is empty")
        return
    print("Items list:")
    for id_, data in items_dict.items():
        print(f"ID: {id_}, Name: {data['name']}, Price: {data['price']}, Quantity: {data['quantity']}")

def main():
    while True:
        print("\n--- Inventory CRUD Menu ---")
        print("1) Create item")
        print("2) Read item by id")
        print("3) Update item by id")
        print("4) Delete item by id")
        print("5) List all items")
        print("0) Exit")
        option = input("Select an option: ").strip()

        if option not in {"0","1","2","3","4","5"}:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Exiting program...")
            break

        if option == "1":  # CREATE
            item_id = input("Enter item id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                if price < 0 or quantity < 0:
                    raise ValueError
            except ValueError:
                print("Error: invalid input")
                continue
            if create_item(items, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: item id already exists")

        elif option == "2":  # READ
            item_id = input("Enter item id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue
            item = read_item(items, item_id)
            if item:
                print(f"ID: {item_id}, Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
            else:
                print("Item not found")

        elif option == "3":  # UPDATE
            item_id = input("Enter item id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue
            if item_id not in items:
                print("Item not found")
                continue
            name = input("Enter new item name: ").strip()
            try:
                price = float(input("Enter new item price: "))
                quantity = int(input("Enter new item quantity: "))
                if price < 0 or quantity < 0:
                    raise ValueError
            except ValueError:
                print("Error: invalid input")
                continue
            if update_item(items, item_id, name, price, quantity):
                print("Item updated")
            else:
                print("Item not found")

        elif option == "4":  # DELETE
            item_id = input("Enter item id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue
            if delete_item(items, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        elif option == "5":  # LIST
            list_items(items)

if __name__ == "__main__":
    main()


"""
Conclusiones:
El uso de funciones facilitó la implementación del CRUD al separar responsabilidades 
y hacer el código más organizado.
La estructura de diccionario permite búsquedas rápidas y evitó duplicados de manera
natural.
Validar las entradas es muy importante para evitar datos inválidos.
Cada función es reutilizable, lo que permite extender el CRUD fácilmente a 
sistemas más grandes.
Este programa podría ampliarse para guardar y cargar datos desde archivos o bases de 
datos en el futuro.
"""

"""
Referencias: 
# 1) Python documentation Data structures (dict, list)
#    https://docs.python.org/3/tutorial/datastructures.html
# 2) Python documentation Defining functions
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 3) W3Schools Python CRUD Tutorial
#    https://www.w3schools.com/python/python_mysql_create_table.asp
"""