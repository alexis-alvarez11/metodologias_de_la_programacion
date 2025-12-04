
# simple dictionary
alien_0= {'color': 'green', 'points': 5}

#The simples dictionary
alien_1= {'color': 'yellow'}

#Accessing values in a dictionary
print(alien_1['color'])
print(alien_0['points'])

#Empty dictionary
alien_2= {}     #NO es necesaria

#Modifying values in a dictionary
alien_2= {'color': 'red'}
alien_2['color']= 'blue'

#Adding new key-value pairs
alien_2['x_ position']= 0
alien_2['y_position']= 25
print(alien_2)

##Dictionary to store similar objects
favorite_languages= {
    'jen': 'python',
    'sarah': 'c',
    'edwar': 'ruby',
}

#print(f"sarah favorite language is {favorite_languages['sarah']}")

#Looping through all key-value pairs
for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite \
language is {value.title()}")
    

for key in favorite_languages.keys():
    print(key)

#Looping through all values
for value in favorite_languages.values():
    print(value)

# Nesting dictionaries

## Listas de diccionarios
## Listas en diccionarios
## Diccionarios en diccionarios


#Diccionario
brawler_colt= {
    "color": "red",
    "weapon": "gun",
    "armament": "nothing",
    "health": "2200"
}

brawler_piper= {
    "color": "blue",
    "weapon": "umbrella",
    "armament": "nothing",
    "health": "2000"
}

brawler_bull= {
    "color": "black",
    "weapon": "shotgun",
    "armament": "nothing",
    "health": "3200"
}

## Listas de diccionarios
brawlers= [
    brawler_colt,
    brawler_piper, 
    brawler_bull
]

for brawler in brawlers:
    print("\n", brawler)
    for key, value in brawler.items():
        print(key, value)
    print()

## Listas en diccionarios
students= {
    "Alexis": ["inteligente", "guapo", "bueno"],
    "Jesus": ["alto", "traidor", "falso"],
    "Pequeño": ["bot", "fan", "pro"]
}

## Diccionarios en diccionarios
sensors= {
    "temperature": {
        "id": "tension",
        "location": "aula 104",
        "value": 25,
        "unit": "celsius"
    },
    "humedad": {
        "id": "hum_1",
        "location": "aula_103",
        "value": 60,
        "unit": "porcentaje"
    }
}
print("temperature")
print(sensors["temperature"]["value"])
print("ubicacion")
print(sensors["temperature"]["location"])

#Metodo get() de los diccionarios