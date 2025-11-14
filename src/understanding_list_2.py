#SLICING
players= ["cr7", 'messi', 'Travis', 'vega', 'corona']
print(players[0:3])

# SLICE: quita el ultimo elemento, segun el que asigne
# slice es trabajar con un grupo especifico de elementos de una lista


print(players[1:4]) # messi, travis, chicha
print(players[:4])  # cr7, messi, Travis, vega
print(players[2:])

print(players[-3:])
print(players[-3:-1:])
print(players[3:4])


#Slicing en for 
players= ["alexis", "cr7", 'messi', 'Travis', 'vega', 'corona']
first_three_players= players[0:3]
print("First three players: ", first_three_players)

print("Aqui vienen los tres mejores del salon: ")
for player in players [0:3]:
    print(player.upper())

#copia lista
my_food= ['pizza', 'gorditas', 'machacaado']
# copy_of_food= my_food  #manera erronea de copiar una lista
copy_of_food_1= my_food[:]
copy_of_food_2= my_food.copy()
copy_of_food_3= list(my_food)


"""
listas: es mutable, puedo alterar
tuplas: listas inmutables, no append, insert (almacena datos inmutables)
"""

# Modificando elementos
cars= ['bwm', 'porch', 'masda' 'totoya', 'ford']
cars[0]= "bmw"
cars[1]= "porshe"
cars[2]= "mazda"
cars[3]= 'toyota'