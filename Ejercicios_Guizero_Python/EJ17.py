from guizero import App, Text, TextBox, PushButton

# Variables
n = 0
numeros = []
resultado = 0
count = 0

# Función para manejar la opción seleccionada
def opcion():
    try:
        opcion = int(opc.value)
        if opcion == 5:
            app.destroy()
        elif opcion < 1 or opcion > 4:
            app.error("Error", "Ingrese una opción válida (1-4).")
        else:
            Texto_1.show()
            entrada_n.show()
            boton_ingresar_n.show()
    except ValueError:
        app.error("Error", "Ingrese un número ")
      
      
# Función para manejar el ingreso de n
def ingresar_n():
    global n
    try:
        n = int(entrada_n.value)
        if n <= 0:
            app.error("Error", "Ingrese un número válido y mayor que 0.")
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
            Operaciones()
    except ValueError:
        app.error("Error", "Ingrese un número válido.")


#Funcion restaurar la interfaz
def reiniciar_sistema():
    global n, numeros, resultado, count
    n = 0
    numeros = []
    resultado = 0
    count = 0
    opc.value =""

    mensaje_resultado.value = ""
    entrada_numero.value = ""
    entrada_n.value = ""


    boton_ingresar_numero.hide()
    entrada_numero.hide()


# Función para realizar la operación seleccionada
def Operaciones():
    global resultado
    if opc.value == "1":
        resultado = sum(numeros)
    elif opc.value == "2":
        resultado = numeros[0] - sum(numeros[1:])
    elif opc.value == "3":
        resultado = 1
        for num in numeros:
            resultado *= num
    elif opc.value == "4":
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado /= num
    app.info("Resultado", f"El resultado es: {resultado}")
    reiniciar_sistema()
    entrada_numero.hide()







app = App("Ejercicio 17")

# Elementos de la interfaz
enunciado1 = Text(app, text="Ejercicio 17\n")
enunciado2 = Text(app, "Selecciona una operación:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")

opc = TextBox(app, width=10)
boton_opc= PushButton(app, text="Ingresar opcion", command=opcion)
espacio1 = Text(app, text="\n") 
Texto_1 = Text(app, "Ingrese la cantidad de números (n):")
entrada_n = TextBox(app, width=10)

boton_ingresar_n = PushButton(app, text="Ingresar n", command=ingresar_n)
entrada_numero = TextBox(app, width=10)

boton_ingresar_numero = PushButton(app, text="Ingresar número", command=ingresar_numero)
mensaje_resultado = Text(app, "")



# Deshabilitar elementos al inicio
Texto_1.hide()
entrada_n.hide() 
boton_ingresar_n.hide()

entrada_numero.hide()
boton_ingresar_numero.hide()



app.display()
