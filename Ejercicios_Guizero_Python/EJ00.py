from guizero import App, PushButton,Text

def mostrar_mensaje():
    app.info("Mensaje", "¡Hola Mundo!")

app = App("Ejercicio 0",width=300, height=100)

enunciado = Text(app, text="Ejercicio 0\n")
boton_hola_mundo = PushButton(app, text="Mostrar mensaje", command=mostrar_mensaje)

app.display()
