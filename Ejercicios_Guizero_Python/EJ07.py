from guizero import App, Text, TextBox, PushButton
# ELIO GABRIEL MARTINEZ RODRIGUEZ 1B

def cuadrado():
    valor = Cuadrado.value
    try:
        valor = float(valor)
        if valor >= 0:
            resultado = valor ** 2
            mensaje_cuadrado.value = (f"El cuadrado es {resultado:.2f}")
        else:
            app.error("Error", "Ingresa un número positivo.")
    except ValueError:
        app.error("Error", "Ingresa un número válido.")

app = App(title="Ejercicio 7")

# Crear elementos
enunciado1 = Text(app, text="Ejercicio 7\n")
enunciado2 = Text(app, "Calcular el cuadrado de un número")

Text1 = Text(app, text="Dame un número:")
Cuadrado = TextBox(app, width=50, height=1)

boton_calcular = PushButton(app, text="Calcular", command=cuadrado)
mensaje_cuadrado = Text(app, text="")
espacio1 = Text(app, text=" ") 

# Botón de cierre
cerrar_boton = PushButton(app, text="Cerrar", command=app.destroy)

app.display()
