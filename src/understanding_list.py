#Listas
#Una lista es una coleccion ordenada y mutable de elementos.
#Se definen utilizando corchetes [] y separando los elementos con comas
#Ejemplo de creacion de una lista: 
fruits= ['manzana', 'banana', 'cereza']
print(fruits) #salida: ['manzana', 'banana', 'cereza']

#Acceso  a elementos
print(fruits[0].upper()) #salida: manzana
print(fruits[2].title()) #salida: cereza

# print(fruits[3]) # Generaria un error fuera de rango

#Acceder al ultimo elemento
print(fruits[-1]) #Salida: cereza
print(fruits[-2]) #Salida: banana
print(fruits[-3]) #Salida: manzana

my_favorite_fruit= fruits[0]
message= f'Mi fruta favorita es la {fruits[0].title()}.'
print(message) # Salida: Mi fruta favorita es la Manzana.

"""
Agregar elementos a la lista
 -append(): Agrega un elemento al final de la lista.
 El metodo append(elemento) toma un solo argumento, que es el elemento que se desea agregar 
 a la lista.
"""
print("\n Agregar elemntos a una lista: Metodo append() \n")
motorcycles=  ['Honda', 'Yamaha', 'Susuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)


"""
 - Insert: Inserta un elemento en una posicion especifica de la lista.
 El metodo insert(index, element) toma dos argumentos:
 el indice donde se desea insertar el elemento y el elemento en si.
"""
print("\n Agregar elementos a una lista: metodo insert() \n")
motorcycles= ['Honda', 'Yamaha', 'Susuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
print(motorcycles[0])


"""
Eliminar elementos  de una lista
- del: Elimina un elemnto en una posicion especifica de la lista. 
La delaracion del index elimina el elemento en la posicion especificada.
"""
print("\n Eliminar elemnetos de una lista: Declaracion del \n")
motorcycles= ['honda', 'yamaha', 'susuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)


"""
Eliminar elemntos de una lista
-pop(): Elimina y devuelve el ultimo eemnto de la lista.
El metodo pop() no requiere argumento y elimina el ultimo elemnto de la lista.
"""
print("\n Eliminar elemntos de una lista Metodo pop() \n")
motorcycles= ['honda', 'yamaha', 'susuki']
print(motorcycles)
popped_motorcycle= motorcycles.pop()
print(motorcycles)

print(f'La motocicleta eliminada es:{popped_motorcycle}. ')

"""
Elimiar elemntos de una lista
 -pop(index): Elimina y devuelve elemnto en una posicion especifica de a lista.
 El metodo pop(index) toma un argumento, que es el indice del elemnto que se desea
 eliminar y devolver.
"""
print("\n Eliminar elementos de una lista: metodo pop(index) \n")
motorcycles= ['honda', 'yamaha', 'susuki']
print(motorcycles)
first_motorcycle= motorcycles.pop(0)
print(motorcycles)
print(f'La primera motocicleta eliminada es: {first_motorcycle}.')


# del= no guarda variable
#pop= solo borra ultimo elemento y con (num) elemento elegido

"""
Elimianr elementos de una lista
 -remove(): elimina la primera aparicion de un valor especifico en la lista.
 el metodo remove(value) toma un elemnto, que es el valor del elemento que se desea eliminar.
"""

print("\n Eliminar elementos de una lista: metodo remove() \n")
motorcycles= ['honda', 'yamaha', 'susuki', 'ducati', 'yamaha']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


#Ejemplo practico de remove()
names= ['ana', 'juan', 'pedro', 'maria', 'juan']
print(names)
deleted_name= input("\n Ingrese el nombre que desea eliminar de la lista: ")
names.remove(deleted_name.strip().lower())
print(names)


"""
ordenar listas

Metodo de las listas: sort()
Ordenamiento permanente, es decir, ordena la lista permanente.

"""
cars= ["bmw", "audi", "ford", "kia"]
print(cars)
cars.sort()
print(cars) # salida: ['audi', 'bmw', 'ford', 'kia']
# con: reverse= True (ordena de Z a A, con False de A a Z, pero no es necesario)

"""
Metodo reverse 
"""
motorcycles= ['mortalika', 'honda', 'ducati']
print(motorcycles)
motorcycles.reverse()
print(motorcycles)

"""
cantidad de elementos en una lista
metodo built-in: len()
"""
cars= ['ford', 'kia', 'chevrolet']
print("\n Metodo len() \n")
print(len(cars)) # salida: 3

"""
Metodo built-in:
 sorted()
  Ordena una lista temporalmente
"""
favorite_students= ["jorge", "jose", "carlos", "emiliano"]
print(favorite_students)

print("lista ordenada temporalmente: ", sorted(favorite_students, reverse= True)) # salida: ['carlos', 'emiliano', 'jorge', 'jose']
print("lista original: ", favorite_students) # salida: ['jorge', 'jose', 'carlos', 'emiliano']