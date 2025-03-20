imple = "Hola Mundoo"
print(imple)


#h  1
#o  2
#l  3
#a  4
#m  5
#u  6
#n  7
#d  8
#o  9 

holamundo = '"Hola Mundo"' + " desde mi casa"
print(holamundo)

#si queremos imprimer una cadena de texto con comillas dobles
#y que el resultado sea una cadena de texto con comillsa simples
#debemos hacer lo siguiente: "Hola Mundo" -> 'Hola Mundo'

salto = "Hola\nMundo"
print(salto)

salto2 = """Hola Mundo

segunda linea """
print(salto2)

holamundo = "Hola Mundo" + " desde mi casa"

holamundo[5]
print(holamundo[2])
for temp in holamundo:
    print(temp)

print(len(holamundo))

if not len(holamundo) != 0:
    print("La cadena de texto no esta vacia")
else:
    print("La cadena de texto esta vacia")