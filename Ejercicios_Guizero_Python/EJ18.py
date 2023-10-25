from guizero import App, Text
import time

serie = "01"

def generar_serie():
    global serie
    while True:
        serie += "01"
        texto_serie.value = serie
        app.update()
        time.sleep(1)  # Esperar 1 segundo

app = App("Ejercicio 18")
enunciado1 = Text(app, text="Ejercicio 18\n")

enunciado2 = Text(app,"Generador de Serie")
texto_serie = Text(app, serie)

generar_serie()

app.display()
