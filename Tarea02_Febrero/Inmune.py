import random

# Definimos la función objetivo
def objective_function(x):
    return -(x ** 2)  # Encontraremos el mínimo de esta función cuadrática

# Parámetros del algoritmo
population_size = 10
cloning_factor = 5
mutation_rate = 0.1
generations = 50

# Inicialización aleatoria de la población de anticuerpos
population = [random.uniform(-10, 10) for _ in range(population_size)]

# Iteramos a través de las generaciones
for generation in range(generations):
    # Evaluamos la función objetivo para cada anticuerpo
    fitness_values = [objective_function(antibody) for antibody in population]
    
    # Ordenamos los anticuerpos según su aptitud (en este caso, queremos maximizar)
    sorted_population = sorted(zip(population, fitness_values), key=lambda x: x[1], reverse=True)
    
    # Seleccionamos los mejores anticuerpos para clonar
    selected_population = [antibody for antibody, _ in sorted_population[:cloning_factor]]
    
    # Clonamos los anticuerpos seleccionados
    cloned_population = [antibody for antibody in selected_population for _ in range(cloning_factor)]
    
    # Aplicamos mutación a los anticuerpos clonados
    mutated_population = [antibody + random.uniform(-1, 1) * mutation_rate for antibody in cloned_population]
    
    # Reemplazamos la población original por la nueva población mutada
    population = mutated_population

# Seleccionamos el anticuerpo con el mayor valor de aptitud
best_antibody, best_fitness = max(zip(population, [objective_function(antibody) for antibody in population]), key=lambda x: x[1])

print("Mejor solución encontrada:", best_antibody)
print("Valor de la función objetivo en la mejor solución:", best_fitness)