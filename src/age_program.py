age= int(input("Set your age: "))
if age <= 4:
    print("Entrada gratuita")
elif age <=18 and age > 4:
    print("Entrada cuesta $200")
elif age >18:
    print("Entrada cuesta $400")
