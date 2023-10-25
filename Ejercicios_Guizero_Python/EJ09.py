from guizero import App, Text, PushButton
# ELIO GABRIEL MARTINEZ RODRIGUEZ 1B

# Función para calcular la suma de los cuadrados de números pares
def suma_cuadrados_pares():
    suma = sum([numero ** 2 for numero in range(0, 21) if numero % 2 == 0])
    resultado.value = f"La suma de los cuadrados de los números pares es: {suma}"

# Crear la aplicación
app = App("Ejercicio 9")

# Crear elementos de la interfaz
enunciado1 = Text(app, text="Ejercicio 9\n")
enunciado2 = Text(app, "Suma de Cuadrados de Números Pares del 0 al 20:")
resultado = Text(app, "", size=12)

# Botón para calcular la suma
boton_calcular = PushButton(app, text="Calcular Suma", command=suma_cuadrados_pares)

# Botón de cierre
cerrar_button = PushButton(app, text="Cerrar", command=app.destroy)

# Mostrar la aplicación
app.display()
