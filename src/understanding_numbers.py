#Numbers

"""
Integers- Enteros

Son numeros sin punto decimal,
-infty , ..., -2, -1, 0, 1, 2, ..., infty

Ejemplo:

#Tipado dinamico
age = 39

Los podemos sumar (+), restar (-), multiplicar(*) y
dividir (/).

Potencias (**2, **3)

Modulo (Dividendo%Divisor)
"""

number_1= 33
number_2= 13

suma= number_1+number_2
difference= number_1-number_2
multiplication= number_1*number_2
division= number_1/number_2
modulo= number_1%number_2
power= number_1**2

print("suma: ", suma)
print("difference: ", difference)
print("multiplication: ", multiplication)
print("division: ", division)
print("modulo: ", modulo)
print("power: ", power)

print("La resta es del tipo ", type(suma))
print("La difference ", type(difference))
print("La multiplicacion es del tipo ", type(multiplication))
print("La division es del tipo ", type(division))
print("La modulo es del tipo ", type(modulo))
print("La power es del tipo ", type(power))

#Floats

"""
Floats-reales

Son numeros con punto decimal,
-van desde -infty  infty

Ejemplo:

#Tipado dinamico
age = 25.5

Los podemos sumar (+), restar (-), multiplicar(*) y
dividir (/).

"""
print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(2*0.2)

print(0.1+0.2)
print(3*0.1)
