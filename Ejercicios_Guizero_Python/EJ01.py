from guizero import App, Box, Text, PushButton
import random

# ELIO GABRIEL MARTINEZ RODRIGUEZ 1B

# Función para generar números aleatorios y calcular el promedio
def generar_y_calcular_promedio():
    # Generar una lista de 10 números aleatorios entre 1 y 100
    numeros = [random.randint(1, 100) for _ in range(10)]
    # Calcular el promedio de la lista de números
    promedio = sum(numeros) / len(numeros)
    
    # Mostrar los números generados
    numeros_generados.value = "Números generados: " + ", ".join(map(str, numeros))
    
    # Mostrar el promedio
    Promedio.value = (f"El promedio es: {promedio:.2f}")

app = App("Ejercicio 1")



# Crear elementos
enunciado = Text(app, text="Ejercicio 1\n")
generar_button = PushButton(app, text="Generar Números y Calcular", command=generar_y_calcular_promedio)
numeros_generados = Text(app, text="")
Promedio = Text(app, text="")

# Botón de cierre
cerrar= PushButton(app, text="Cerrar", command=app.destroy)

app.display()
