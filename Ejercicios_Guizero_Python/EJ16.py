from guizero import App, Text, PushButton, Box

# Inicializar diccionario para realizar seguimiento de productos vendidos
productos_vendidos = {"Torta": 0, "Tacos": 0, "Hotdog": 0, "Pizza": 0}

# Función para manejar la venta de productos
def vender_producto(producto):
    productos_vendidos[producto] += 1
    actualizar_estadisticas()

# Función para mostrar las estadísticas
def actualizar_estadisticas():
    mensaje_resultado.value = "Estadísticas de venta:\n"
    for producto, cantidad in productos_vendidos.items():
        mensaje_resultado.value += f"{producto}: {cantidad}\n"

# Función para finalizar y mostrar el total de productos vendidos
def finalizar_venta():
    actualizar_estadisticas()
    boton_torta.hide()
    boton_tacos.hide()
    boton_hotdog.hide()
    boton_pizza.hide()
    boton_finalizar.hide()
    mensaje_resultado.value += f"\nTotal de productos vendidos: {sum(productos_vendidos.values())}"

app = App("Ejercicio 16")

enunciado1 = Text(app, text="Ejercicio 16\n")
enunciado = Text(app, text="Venta de Productos")
enunciado2 = Text(app, "Selecciona los productos vendidos por los usuarios:")

boton_torta = PushButton(app, text="Torta", command=lambda: vender_producto("Torta"))
boton_tacos = PushButton(app, text="Tacos", command=lambda: vender_producto("Tacos"))
boton_hotdog = PushButton(app, text="Hotdog", command=lambda: vender_producto("Hotdog"))
boton_pizza = PushButton(app, text="Pizza", command=lambda: vender_producto("Pizza"))
boton_finalizar = PushButton(app, text="Finalizar", command=finalizar_venta)

mensaje_resultado = Text(app, "")

cerrar_button = PushButton(app, text="Cerrar", command=app.destroy)
app.display()
