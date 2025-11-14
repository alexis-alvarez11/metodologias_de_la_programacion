#List comprenhensions

"""
Una lista comprenhension combia el for looop y la creacion de nuevos elementos en una 
sola linea de codigo y tambien, automaticamente agrega el nuevo elemento a la lista, 
es decir sin utilizar el append.
"""

"""
comparacion logica: ==
asignacion: =
"""

squares= [value**2 for value in range(1, 11)]
print(squares)


#numeros pares con el range
even_numbers_0_100= list(range(0,101,2))
print(even_numbers_0_100)

#numeros pares usando list comprenhension
evens_list_compre= [value for value in range(0,101) if value%2 ==0]
print(evens_list_compre)
