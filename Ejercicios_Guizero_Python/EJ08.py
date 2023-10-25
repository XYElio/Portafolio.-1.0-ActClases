from guizero import App, Text, PushButton
# ELIO GABRIEL MARTINEZ RODRIGUEZ 1B

# Función para encontrar y mostrar los números pares
def encontrar_numeros_pares():
    pares = [str(numero) for numero in range(0, 21) if numero % 2 == 0]
    resultado.value = ", ".join(pares)

# Crear la aplicación
app = App("Ejercicio 8")

# Crear elementos de la interfaz
enunciado1 = Text(app, text="Ejercicio 8\n")
enunciado2 = Text(app, "Números Pares del 0 al 20:")
resultado = Text(app, "", size=12)

# Botón para encontrar números pares
boton_encontrar = PushButton(app, text="Mostrar Números Pares", command=encontrar_numeros_pares)

# Botón de cierre
cerrar_button = PushButton(app, text="Cerrar", command=app.destroy)

# Mostrar la aplicación
app.display()
