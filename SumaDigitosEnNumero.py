numero = input("Ingresa un número: ")
suma_digitos = 0

for digito in numero:
    suma_digitos += int(digito)

print("La suma de los dígitos es:", suma_digitos)
