
# EXAMEN U2 VERSION 2C

CORRECT_PIN= "admin123"
MAX_ATTEMPTS= 3
intents= 0

while intents < MAX_ATTEMPTS:

    user_pin= input("Enter your password: ")
    if user_pin == CORRECT_PIN:
        print("Access autorized")
        break
    
    else: 
        intents +=1
        remaining= MAX_ATTEMPTS - intents
        if remaining > 0:
            print(f"Incorrect answer, intents: {remaining}")
        else: 
            print("Access Denegade")



# PREGUNTA RESCATE


n= int(input("Enter your number: "))
if not n:
    print("Error: Invalid input")
    exit()

if n < 1 or n > 50:
    print("Error: Incorrect values")
    exit()

f1= 0
f2= 1

if n == 1:
    print(f1)

print("The Fibonacci series is:", n)
print("Fibonacci series end in: ", end= " " )

if n== 1:
    print(f1)
elif n== 2:
    print(f1, f2)
else: 
    print(f1, f2, end="")
    for i in range(3, n + 1):
        fn= f1 + f2
        print(fn, end=" ")
        f1= f2
        f2= fn




