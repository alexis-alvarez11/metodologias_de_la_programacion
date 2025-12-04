"""
Las tuplas son listas de elemnetos que no pueden cambiar
en su tamaño, tuplas son listas inmutables.

Se utilizan los() para definir una tupla.
Ejemplo:
"""

#rectangulo (largo, ancho)
rectangle_dimensions= (200,50) #tupla
print(rectangle_dimensions)
print(f"largo: {rectangle_dimensions[0]}") #200
print(f"ancho: {rectangle_dimensions[1]}") #50

#intentar modificar una tupla
#rectangle_dimensions[0]=250 #TypeError: 'tuple'
#rectangle_dimensions[1]=100 #TypeError: 'tuple'

for dimension in rectangle_dimensions:
    print(dimension)

"""
No podemos modificar los elementos de una tupla, ni agregar/eliminar
elementos. LO que si podemos hacer es cambiar la asignacion 
a una variable que almacena una tupla.

(le reasigno valor, a la misma tupla)
"""

rectangle_dimensions= (300, 150) #Tupla
