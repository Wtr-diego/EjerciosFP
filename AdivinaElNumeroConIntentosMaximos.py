import random
import tkinter as tk
from tkinter import messagebox

# Generamos un número aleatorio entre 1 y 100
numero = random.randint(1, 100)
intentos = 0
max_intentos = 8

# Función para manejar los intentos del usuario
def verificar_numero():
    global intentos
    entrada = entrada_usuario.get()

    # Validar que la entrada sea un número
    if not entrada.isdigit():
        messagebox.showerror("Error", "Debes introducir un número entero")
        return

    intento = int(entrada)
    intentos += 1

    # Comparación con el número secreto
    if intento == numero:
        messagebox.showinfo("¡Felicidades!", f"Has adivinado el número en {intentos} intentos.")
        ventana.destroy()
    elif intentos >= max_intentos:
        messagebox.showwarning("Fin del juego", f"Has agotado los {max_intentos} intentos. El número secreto era {numero}.")
        ventana.destroy()
    elif intento < numero:
        resultado.set("El número secreto es mayor")
    else:
        resultado.set("El número secreto es menor")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Adivina el Número")

# Etiqueta de instrucciones
tk.Label(ventana, text="Adivina el número entre 1 y 100").pack()

# Mostrar intentos restantes
resultado = tk.StringVar()
resultado.set(f"Tienes un máximo de {max_intentos} intentos")
tk.Label(ventana, textvariable=resultado).pack()

# Entrada del usuario
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack()

# Botón para verificar el número
tk.Button(ventana, text="Probar", command=verificar_numero).pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
