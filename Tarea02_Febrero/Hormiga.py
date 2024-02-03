import random

class ColoniaHormigas:
    def __init__(self, cuadricula, inicio, fin, n_hormigas, max_iter):
        self.cuadricula = cuadricula
        self.feromonas_cuadricula = [[1] * len(fila) for fila in cuadricula]
        self.inicio = inicio
        self.fin = fin
        self.n_hormigas = n_hormigas
        self.max_iter = max_iter

    def ejecutar(self):
        for i in range(self.max_iter):
            hormigas = [Hormiga(self) for _ in range(self.n_hormigas)]
            for hormiga in hormigas:
                hormiga.mover()

            self.actualizar_feromonas(hormigas)

            mejor_camino = min(hormigas, key=lambda x: x.distancia_total)
            print(f"Iteración {i + 1}: Mejor camino - {mejor_camino.camino}, Distancia - {mejor_camino.distancia_total}")

    def actualizar_feromonas(self, hormigas):
        tasa_evaporacion = 0.5
        for i, fila in enumerate(self.feromonas_cuadricula):
            for j, feromona in enumerate(fila):
                self.feromonas_cuadricula[i][j] *= (1 - tasa_evaporacion)
                for hormiga in hormigas:
                    if (i, j) in hormiga.camino:
                        self.feromonas_cuadricula[i][j] += 1 / hormiga.distancia_total

class Hormiga:
    def __init__(self, colonia):
        self.colonia = colonia
        self.camino = []
        self.distancia_total = 0
        self.posicion_actual = colonia.inicio

    def mover(self):
        while self.posicion_actual != self.colonia.fin:
            movimientos_posibles = self.obtener_movimientos_posibles()
            probabilidades = self.calcular_probabilidades(movimientos_posibles)
            movimiento = self.seleccionar_movimiento(movimientos_posibles, probabilidades)
            self.camino.append(movimiento)
            self.distancia_total += self.colonia.cuadricula[movimiento[0]][movimiento[1]]
            self.posicion_actual = movimiento

    def obtener_movimientos_posibles(self):
        i, j = self.posicion_actual
        movimientos = []
        if i > 0:
            movimientos.append((i - 1, j))
        if i < len(self.colonia.cuadricula) - 1:
            movimientos.append((i + 1, j))
        if j > 0:
            movimientos.append((i, j - 1))
        if j < len(self.colonia.cuadricula[0]) - 1:
            movimientos.append((i, j + 1))
        return movimientos

    def calcular_probabilidades(self, movimientos_posibles):
        probabilidades = []
        suma_feromonas = sum(self.colonia.feromonas_cuadricula[i][j] for i, j in movimientos_posibles)
        for movimiento in movimientos_posibles:
            i, j = movimiento
            probabilidad = self.colonia.feromonas_cuadricula[i][j] / suma_feromonas
            probabilidades.append(probabilidad)
        return probabilidades

    def seleccionar_movimiento(self, movimientos_posibles, probabilidades):
        movimiento_seleccionado = random.choices(movimientos_posibles, probabilidades)[0]
        return movimiento_seleccionado

# Ejemplo de uso
cuadricula = [
    [1, 3, 1, 2],
    [2, 1, 2, 1],
    [1, 2, 3, 1],
    [2, 1, 1, 2]
]

inicio = (0, 0)
fin = (3, 3)
n_hormigas = 5
max_iter = 10

colonia_hormigas = ColoniaHormigas(cuadricula, inicio, fin, n_hormigas, max_iter)
colonia_hormigas.ejecutar()
