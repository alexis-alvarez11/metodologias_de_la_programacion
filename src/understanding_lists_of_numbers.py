"""
Las listas tambien pueden almacenar numeris y de hecho son  ideales para almacenarlos. 
Python ofrece cantidad de funciones integradas para trabajar con liistas de numeros.

Por ejemplo, funcion range():

"""

# La funcion range() genera una lista de numeros en un rango especifico
#en un rango específico.
#Por ejemplo, para generar una lista de numeros del 0 al 9:
numbers = list(range(10))
print(numbers)  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers))  # Salida: <class 'list'>


#Podemos reaizar lo mismo con un for loop:
for num in range(10):
    print(num)  
    # print (type(num))  # Salida: <class 'int'>


print("\nNumeros del 1 al 4:")
for num in range(1, 5):
    print(num)  
    # print (type(num))  # Salida: <class 'int'>
    numbers_1_to_4 = list(range(1, 5))
print(numbers_1_to_4)  # Salida: [1, 2, 3, 4]


print("\nNumeros impares:")
for num in range(1, 10, 2): #Numeros impares del 1 al 9
    print(num)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)  # Salida: [1, 3, 5, 7, 9]


print("\nNumeros pares:")
for num in range(2, 11, 2): #Numeros pares del 0 al 8
    print(num)  
even_numbers = list(range(2, 11, 2))
print(even_numbers)  # Salida: [2, 4, 6, 10]


# podemos crear cualquier tipo de listas de numeros
# utilizando range() y list()
print("\n primeros 10 numeros al cuadrado")

squares= []
for value in range(1, 11):
    square= value **2
    squares.append(square)
print(squares) # Salida : [1, 4 ,9, 16, 25, 36, 49, 64, 81, 100]


#Metodos built-in paa listas de numeros
print("\n Metodos bulit-in para listas de numeros:")
digits= [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Listas de digitos: {digits}")
print("Valor minimo:", min(digits)) # Salida: 0
print("Valor maximo:", max(digits)) # Salida: 9
print(" Suma de todos lo numeros:", sum(digits)) # Salida: 45


squares_list_comprenhension= [num**2 for num in range(10)]
print(squares_list_comprenhension)
