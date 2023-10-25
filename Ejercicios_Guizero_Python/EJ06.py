from guizero import App, Text, TextBox, PushButton
# ELIO GABRIEL MARTINEZ RODRIGUEZ 1B

# Inicializamos el contador de aprobados
aprobados = 0
desaprobados = 0
calificaciones_ingresadas = 0

def contar_aprobados():
    global aprobados, desaprobados, calificaciones_ingresadas
    calificaciones = entrada_calificaciones.value.split()
    
    if calificaciones_ingresadas + len(calificaciones) > 25:
        resultado.value = ("No se pueden ingresar más de 25 calificaciones en total.\n")
        return
    
    for i in range(len(calificaciones)):
        try:
            calificacion = float(calificaciones[i])
            if 0 <= calificacion <= 10:
                if calificacion >= 7:
                    aprobados += 1
                else:
                    desaprobados += 1
                calificaciones_ingresadas += 1
            else:
                resultado.value = ("Las calificaciones deben estar en el rango de 0 a 10.\n")
                return
        except ValueError:
            resultado.value = ("Ingresa solo calificaciones numéricas válidas.\n")
            return
    
    resultado.value = (f"Calificación {calificaciones_ingresadas} ingresada. Aprobados: {aprobados}, Desaprobados: {desaprobados}\n")
    
    if calificaciones_ingresadas == 25:
        resultado_final()

    # Limpia la caja de entrada para permitir nuevas calificaciones
    entrada_calificaciones.clear()


def resultado_final():
    resultado.value = (f"Aprobados: {aprobados}, Desaprobados: {desaprobados}\n")

def reiniciar():
    global aprobados, desaprobados, calificaciones_ingresadas
    aprobados = 0
    desaprobados = 0
    calificaciones_ingresadas = 0
    resultado.value = ""
    entrada_calificaciones.clear()

app = App("Ejercicio 6")

# Crear elementos de la GUI
enunciado1 = Text(app, text="Ejercicio 6\n")
enunciado2 = Text(app, "Las calificaciones de los alumnos (0-10)\n")
entrada_calificaciones = TextBox(app, width=40)
boton_contar = PushButton(app, text="Contar Aprobados", command=contar_aprobados)
boton_reiniciar = PushButton(app, text="Reiniciar", command=reiniciar)
resultado = Text(app, "")

# Botón de cierre
cerrar_boton = PushButton(app, text="Cerrar", command=app.destroy)

app.display()
