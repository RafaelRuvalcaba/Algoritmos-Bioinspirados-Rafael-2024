import math
import random

def recocido_simulado(estado_inicial, temperatura_inicial, tasa_enfriamiento, iteraciones):
    estado_actual = estado_inicial
    energia_actual = obtener_energia(estado_actual)

    mejor_estado = estado_actual
    mejor_energia = energia_actual

    for i in range(iteraciones):
        temperatura_inicial *= tasa_enfriamiento

        estado_vecino = obtener_estado_vecino(estado_actual)
        energia_vecino = obtener_energia(estado_vecino)

        delta_energia = energia_vecino - energia_actual

        if delta_energia < 0 or random.uniform(0, 1) < math.exp(-delta_energia / temperatura_inicial):
            estado_actual = estado_vecino
            energia_actual = energia_vecino

        if energia_actual < mejor_energia:
            mejor_estado = estado_actual
            mejor_energia = energia_actual

        print(f"Iteración {i + 1}: Mejor Estado - {mejor_estado}, Mejor Energía - {mejor_energia}")

    return mejor_estado

def obtener_energia(estado):
    return estado**2  # Función cuadrática de ejemplo

def obtener_estado_vecino(estado):
    # Genera un estado vecino cambiando ligeramente el estado actual
    return estado + random.uniform(-0.5, 0.5)

# Ejemplo de uso
estado_inicial = 5.0
temperatura_inicial = 1.0
tasa_enfriamiento = 0.95
iteraciones = 100

mejor_estado = recocido_simulado(estado_inicial, temperatura_inicial, tasa_enfriamiento, iteraciones)
print(f"Estado Óptimo: {mejor_estado}, Energía Óptima: {obtener_energia(mejor_estado)}")
