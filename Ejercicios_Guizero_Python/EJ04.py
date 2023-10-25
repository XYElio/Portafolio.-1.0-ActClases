from guizero import App, Text, TextBox, PushButton
# ELIO GABRIEL MARTINEZ RODRIGUEZ 1B

n = 0
numeros = []
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
        mensaje_resultado.value = f"Ingrese {n} números ({count}/{n}):"

        if n > 0:
            entrada_numero.show()
            boton_ingresar_numero.show()
            Texto_1.hide()
            entrada_n.hide()
            boton_ingresar_n.hide()
            
            
        else:
            entrada_numero.hide()
            boton_ingresar_numero.hide()
    except ValueError:
        app.error("Error", "Ingrese un número ")

# Función para ingresar números
def ingresar_numero():
    global count
    try:
        numero = float(entrada_numero.value)
        if numero <= 0:
            app.error("Error", "Ingrese un número válido y mayor que 0.")
            return
        numeros.append(numero)
        entrada_numero.clear()
        count += 1  # Incrementar el contador
        if count <= n:
            mensaje_resultado.value = (f"Ingrese {n} números ({count}/{n}).")
        if count == n:
            boton_ingresar_numero.hide()  # Deshabilitar el botón después de ingresar 'n' números
            calcular_promedio()
    except ValueError:
        app.error("Error", "Ingrese un número válido.")


#Funcion restaurar la interfaz
def reiniciar_sistema():
    global n, numeros, resultado, count
    n = 0
    numeros = []
    resultado = 0
    count = 0

    mensaje_resultado.value = ""
    entrada_numero.value = ""
    entrada_n.value = ""
    entrada_n.show()
    boton_ingresar_n.show()
    boton_ingresar_numero.hide()
    entrada_numero.hide()


# Función para calcular la suma de los cuadrados
def calcular_promedio():
    global resultado
    resultado = sum(numeros) / len(numeros)
    mensaje_resultado.value = (f"El promedio de los números es: {resultado:.2f}")
    entrada_numero.hide()
    boton_reiniciar.show()




app = App("Ejercicio 4")

# Elementos de la interfaz
enunciado1 = Text(app, text="Ejercicio 4\n")
enunciado2 = Text(app, "Obtener el promedio n números.")

Texto_1 = Text(app, "Ingrese la cantidad de números (n):")
entrada_n = TextBox(app, width=10)

boton_ingresar_n = PushButton(app, text="Ingresar n", command=ingresar_n)
entrada_numero = TextBox(app, width=10)

boton_ingresar_numero = PushButton(app, text="Ingresar número", command=ingresar_numero)
mensaje_resultado = Text(app, "")


boton_reiniciar = PushButton(app, text="Reiniciar sistema", command=reiniciar_sistema)

# Deshabilitar elementos al inicio
entrada_numero.hide()
boton_ingresar_numero.hide()
espacio1 = Text(app, text=" ") 
boton_reiniciar.hide()

# Botón de cierre
cerrar_button = PushButton(app, text="Cerrar", command=app.destroy)
app.display()
