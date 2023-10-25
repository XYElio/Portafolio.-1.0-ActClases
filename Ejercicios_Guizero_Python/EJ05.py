from guizero import App, Text, TextBox, PushButton
# ELIO GABRIEL MARTINEZ RODRIGUEZ 1B

# Variables
n = 0
anios_nacimiento = []
resultado = 0
count = 0

# Función para manejar el ingreso de n
def ingresar_n():
    global n
    try:
        n = int(entrada_n.value)
        if n <= 1:
            app.error("Error", "Ingrese un número válido y mayor que 1.")
            return
        mensaje_resultado.value = f"Ingrese los años de nacimiento ({count}/{n}):"

        if n > 0:
            entrada_anio.show()
            boton_ingresar_anio.show()
            Texto_1.hide()
            entrada_n.hide()
            boton_ingresar_n.hide()
    except ValueError:
        app.error("Error", "Ingrese un número válido.")

# Función para ingresar años de nacimiento
def ingresar_anio():
    global count
    try:
        anio = int(entrada_anio.value)
        if anio <= 0 or anio > 2023:
            app.error("Error", "Ingrese un año válido mayor que 0 y menor o igual a 2023.")
            return
        anios_nacimiento.append(anio)
        entrada_anio.clear()
        count += 1  # Incrementar el contador
        if count <= n:
            mensaje_resultado.value = (f"Ingrese los años de nacimiento ({count}/{n}).")
        if count == n:
            boton_ingresar_anio.hide()  # Deshabilitar el botón después de ingresar 'n' años
            calcular_edades()
    except ValueError:
        app.error("Error", "Ingrese un año válido.")

# Función para calcular edades
def calcular_edades():
    global resultado
    edades = [2023 - anio for anio in anios_nacimiento]
    resultado = sum(edades) / len(edades)
    mensaje_resultado.value = (f"El promedio de edades es: {resultado:.2f}")
    entrada_anio.hide()
    boton_reiniciar.show()

# Función para reiniciar la interfaz
def reiniciar_sistema():
    global n, anios_nacimiento, resultado, count
    n = 0
    anios_nacimiento = []
    resultado = 0
    count = 0

    mensaje_resultado.value = ""
    entrada_anio.value = ""
    entrada_n.value = ""
    entrada_n.show()
    boton_ingresar_n.show()
    boton_ingresar_anio.hide()
    entrada_anio.hide()

app = App("Ejercicio 5")

# Elementos de la interfaz
enunciado1 = Text(app, text="Ejercicio 5\n")
enunciado2 = Text(app, "Calcular el promedio de edades")

Texto_1 = Text(app, "Ingrese la cantidad de personas (n):")
entrada_n = TextBox(app, width=10)

boton_ingresar_n = PushButton(app, text="Ingresar n", command=ingresar_n)
entrada_anio = TextBox(app, width=10)

boton_ingresar_anio = PushButton(app, text="Ingresar año", command=ingresar_anio)
mensaje_resultado = Text(app, "")

boton_reiniciar = PushButton(app, text="Reiniciar sistema", command=reiniciar_sistema)

# Deshabilitar elementos al inicio
entrada_anio.hide()
boton_ingresar_anio.hide()
espacio1 = Text(app, text=" ") 
boton_reiniciar.hide()

# Botón de cierre
cerrar_button = PushButton(app, text="Cerrar", command=app.destroy)
app.display()
