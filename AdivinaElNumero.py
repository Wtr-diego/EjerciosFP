import random # Importamos la librería random
numero_secreto = random.randint(1, 100) # Generamos un número aleatorio entre 1 y 100
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número secreto: ")) # Solicitamos al usuario que adivine el número secreto
    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número secreto.")
        adivinado = True
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")