from guizero import App, Text, TextBox, PushButton



# Función para calcular la suma de números válidos
def calcular_suma():
    numeros_validos = []
    for i in range(5):
        numero = entrada_numeros[i].value
        try:
            numero = float(numero)
            if 5 <= numero <= 10:
                numeros_validos.append(numero)
            else:
                app.info("Información", "El número en la campo" + str(i+1) + " debe estar dentro del rango de 5 a 10.")
        except ValueError:
            app.info("Información", "Ingrese un valor numérico válido en la casilla " + str(i+1))

    if len(numeros_validos) == 5:
        suma = sum(numeros_validos)
        resultado.value = (f"Suma de números : {suma}")

# Función para restablecer el programa
def reiniciar_sistema():
    for entrada in entrada_numeros:
        entrada.value = ""
    resultado.value = ""
    resultado_validos.value = ""

# Crear la aplicación
app = App("Ejercicio 13\n")

# Crear elementos
enunciado1 = Text(app, text="Ejercicio 13 \n")
enunciado2 = Text(app, "Ingrese 5 números entre 5 y 10 (inclusive):")

entrada_numeros = [TextBox(app, width=5) for _ in range(5)]
resultado = Text(app, "")
resultado_validos = Text(app, "")

# Botón para calcular la suma
boton_calcular = PushButton(app, text="Calcular Suma", command=calcular_suma)

# Botón para restablecer
boton_reiniciar = PushButton(app, text="Reiniciar sistema", command=reiniciar_sistema)

# Botón de cierre
cerrar_button = PushButton(app, text="Cerrar", command=app.destroy)

# Mostrar la aplicación
app.display()
