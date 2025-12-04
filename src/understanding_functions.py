"""
    Functions
    Las funciones son bloques de codigo diseñados
    para realizar una tarea especifica.

    Cuando queremos realizar la tarea que se ha definido 
    en una funcion, tenemos que llamar el nombre de la funcion 
    responsable de esto.

    Definicion de una funcion (Syntax)

    def name_of_function(parameters):
        actions
"""
def greeting_alexis():
    print("Hola Alexis, que gusto verte!!")


# Parametros
def greet(username, msj):
    print(f"Hola {username}, {msj} que bueno verte!!")

# Argumentos
greeting_alexis()
greet("Eduardo", "que pro")

"""
    Vamos a realizar un  programa que genere 
    el nombre completo de una persona.

    Pasar el primer nombre, el segundo y el apellido.

    La funcion debe generar el nombre completoo
    y regresarlo,
"""

def creat_full_name(first_name, last_name, middle_name=""):
    """
        Docstring - This function creates the fullname 
        of a person given its three names.
    """
    full_name= f"{first_name} {middle_name} {last_name}"
    return full_name.title()

user_first_name= input("Primer nombre: ").strip().lower()
user_middle_name= input("Segundo nombre: ").strip().lower()
user_last_name= input("Apellidos: ").strip().lower()

# Argumentos Posicionales -> Positional Arguments
print(creat_full_name(
    user_first_name,  
    user_last_name,
    user_middle_name,
    ))

# Argumentos Posicionales -> Positional Arguments
full_name= creat_full_name(
    user_first_name,
    user_last_name,
    user_middle_name
)
print(full_name)

# Argumentos clave -> Keyword Arguments
full_name_key= creat_full_name(
    last_name= user_last_name, 
    first_name= user_first_name,
    middle_name= user_middle_name
)
print(full_name)

## Parametros Opcionales
profe_falso = creat_full_name(user_first_name, user_last_name)
print(profe_falso)

# funciones: args, kwargs
# manejo de datoss: abrir archivos csv, .json, .yml
# cli - command line interface
# generadores, iteradores, yield
# testing ->
# argumentos por linea de comando- sys