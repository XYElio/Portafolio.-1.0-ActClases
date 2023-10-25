from guizero import App, Text, TextBox, PushButton

# ELIO GABRIEL MARTINEZ RODRIGUEZ 1B


# Función para calcular la edad
def calcular_edad():
    # Obtener el año de nacimiento y el año actual desde las entradas de texto
    anio_nacimiento = a_nacimiento.value
    anio_actual = a_actual.value

    if anio_nacimiento.isdigit() and anio_actual.isdigit():
        anio_nacimiento = int(anio_nacimiento)
        anio_actual = int(anio_actual)
        
        if anio_nacimiento >= 0 and anio_actual >= 0:
            if anio_actual >= anio_nacimiento:
                # Calcular la edad
                edad = anio_actual - anio_nacimiento
                texto_edad.value = (f"Tu edad correspondiente es {edad} años.")
            else:
                texto_edad.value = ""
                app.error("Error", "El año de nacimiento debe ser menor o igual al año actual.")
        else:
            texto_edad.value = ""
            app.error("Error", "Ingresa años positivos.")
    else:
        texto_edad.value = ""
        app.error("Error", "Ingresa años válidos.")

app = App("Ejercicio 2 y 3")

# Crear elementos
enunciado1 = Text(app, text="Ejercicio 2 y 3\n")
enunciado2 = Text(app, "Calculadora de Edad")

Texto1 = Text(app, "Ingresa tu año de nacimiento:")
a_nacimiento = TextBox(app)

Texto2 = Text(app, "Ingresa el año actual:")
a_actual = TextBox(app)

calcular = PushButton(app, text="Calcular Edad", command=calcular_edad)
texto_edad = Text(app, text="")

# Botón de cierre
cerrar_button = PushButton(app, text="Cerrar", command=app.destroy)

app.display()
