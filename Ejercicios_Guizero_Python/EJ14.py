from guizero import App, Text, TextBox, PushButton

# Variables
n = 0
numeros = []
resultado = 0
count = 0

# Función para manejar el ingreso de n
def ingresar_n():
    global n
    try:
        n = int(entrada_n.value)
        if n <= 0:
            app.error("Error", "Ingrese un número válido y mayor que 0.")
            return
        mensaje_resultado.value = f"Ingrese {n} sueldos base del empleado  ({count}/{n}):"

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
            mensaje_resultado.value = (f"Ingrese {n} sueldos base del empleado ({count}/{n}).")
        if count == n:
            boton_ingresar_numero.hide()  # Deshabilitar el botón después de ingresar 'n' números
            calcular_sueldo_total(numero)
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




def calcular_sueldo_total(sueldo_base):
    
    totalSueldos = 0
    totalImpuesto = 0

    for sueldo_base in numeros:
        canastaB = sueldo_base * 0.05
        primaA = sueldo_base * 0.03 if sueldo_base > 10000 else 0

        if sueldo_base > 10000:
            ISR = sueldo_base * 0.3
        else:
            ISR = sueldo_base * 0.2

        sueldo_total = sueldo_base + canastaB + primaA

        totalSueldos += sueldo_total - ISR
        totalImpuesto += ISR

    mensaje_resultado.value = (
        f"El sueldo total a pagar a todos los empleados es: {totalSueldos:.2f}\n"
        f"El total de impuestos a pagar al SAT es: {totalImpuesto:.2f}"
    )

    entrada_numero.hide()
    boton_reiniciar.show()


app = App("Ejercicio 14")

# Elementos de la interfaz
enunciado1 = Text(app, text="Ejercicio 14\n")
enunciado2 = Text(app, "Calcular Nomina.")

Texto_1 = Text(app, "Ingresa la cantidad de empleados:")
entrada_n = TextBox(app, width=10)

boton_ingresar_n = PushButton(app, text="Ingresar empleados", command=ingresar_n)
entrada_numero = TextBox(app, width=10)

boton_ingresar_numero = PushButton(app, text="Ingresa el sueldo", command=ingresar_numero)
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
