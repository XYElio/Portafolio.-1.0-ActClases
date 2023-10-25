from guizero import App, Text, TextBox, PushButton

def determinar_dia_semana():
    numero = int(entrada_numero.value)
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    if 1 <= numero <= 7:
        dia = dias_semana[numero - 1]
        mensaje_resultado.value = (f"El día correspondiente al número {numero} es: {dia}")
    else:
        mensaje_resultado.value = "Número fuera del rango válido (1 al 7)."

app = App("Ejercicio 15")

enunciado1 = Text(app, text="Ejercicio 15\n")
enunciado1 = Text(app, text="Determinar Día de la Semana \n")
enunciado2 = Text(app, "Ingresa un número del 1 al 7 para determinar el día de la semana.")

Texto1 = Text(app, "Ingresa un número:")
entrada_numero = TextBox(app)

boton_determinar = PushButton(app, text="Determinar Día", command=determinar_dia_semana)
mensaje_resultado = Text(app, "")


cerrar_button = PushButton(app, text="Cerrar", command=app.destroy)
app.display()
