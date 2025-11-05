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
 -append(): Agrega un elemento al final de la lista
"""
print("\n Agregar elemntos a un alista: Metodo append() \n")
motorcycles=  ['Honda', 'Yamaha', 'Susuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)


"""
 - Insert: Inserta un elemento en una posicion especifica de la lista.
"""
print("\n Agregar elementos a una lista: metodo insert() \n")
motorcycles= ['Honda', 'Yamaha', 'Susuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
print(motorcycles[0])

