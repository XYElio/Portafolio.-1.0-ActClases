from guizero import App, Text, PushButton, TextBox
import time

serie = ""
n = 0

def generar_serie():
    global serie, n
    while n > 0:
        serie += "01"
        texto_serie.value = serie
        app.update()
        n -= 1
        time.sleep(1)

def iniciar_generacion():
    global n
    try:
        n = int(repeticiones.value)  # Obtener el número de repeticiones del campo de entrada
        if n < 0:
            raise ValueError("El número de repeticiones debe ser mayor o igual a 0")
        texto_serie.clear()
        generar_serie()
    except ValueError as error:
        texto_serie.clear()
        texto_serie.value = f"Error: {error}"

app = App("Ejercicio 18")
enunciado1 = Text(app, text="Ejercicio 19\n")
enunciado2 = Text(app,"Generador de Serie")

repeticiones_label = Text(app, "Repeticiones:")
repeticiones = TextBox(app)
boton_generar = PushButton(app, text="Iniciar Generación", command=iniciar_generacion)
texto_serie = Text(app, serie)

app.display()


