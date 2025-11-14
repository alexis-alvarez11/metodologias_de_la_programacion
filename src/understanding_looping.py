magicians= ["ron", "harry", "hermione", "snape"]

for magician in magicians:
    print(magician)    
    print(magician.upper())
    print(f"{magician.title()} that was a great trick!")
    print("\n")
print("Gracias a todos, gran espectaculo")

"""
    Identacion 
    Python utiliza la identacion para determinar cuando un alinea 
    de codigo esta conectada a la linea de codigo anterior.

   Basicamente, se utilizan 4 espacios en blanco para 
   obligarnos a escribir codigo ordenado y estructurado.
    
"""

#No olvidemos identar (donde se necesita)
#ejemplo
magicians= ['alice', 'david', 'jorge']
for magician in magicians:
#print(magician) #Error- El for necesita al menos un elemento identado
    print(magician) #solucion


#identation error
#logical error
magicians= ['alice', 'david', 'jorge', 'candelario']
for magician in magicians:
    print(magician)
#print(f"Great {magician}! I can't wait to see your next trick")
    print(f"Great {magician}! I can't wait to see your next trick")


    #identacion innecesaria
message= "Hello Alexis!"
print(message)
#print(message) #Error- identacion innecesaria

magicians= ['alice', 'david', 'jorge', 'candelario']
for magician in magicians:
    print(magician)
    print(f"Great {magician}! I can't wait to see your next trick")
print("Thank you everyone, that was a great magic show!") #solucion identar a izquierda

#error de sintaxis
magicians= ['alice', 'david', 'jorge', 'candelario']
for magician in magicians:# (syntaxisError): olvidar poner los dos puntos (:)
    print(magician)

