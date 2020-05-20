# Exercício 1

import numpy as np

# Dadas as seguintes séries temporais
s1 = np.array([168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 323, 106, 1055, 170])

s2 = np.array([168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 180, 106, 1055, 200])

# Definindo uma função para calcular a distância euclidiana entre as séries
def dist(s1, s2):
    a = np.sqrt(np.sum((s1-s2)**2))
    return a

dist_eu = dist(s1, s2)

print("Array1:\n", s1)
print("")
print("Array2:\n", s2)
print("")
print("Distancia Euclidiana:\n", dist_eu)
print("")

# Calcular a série temporal com os valores médios entre s1 e s2
ar = s1, s2
print("Média entre as séries:\n", np.mean(ar, axis=0))
print("")

# Calcular a série temporal com os valores máximos de cada instante entre s1 e s2
print("Valores máximos:\n", np.maximum(s1, s2))
print("")

# Calcular a série temporal com os valores mínimos de cada instante entre s1 e s2
print("Valores mínimos:\n", np.minimum(s1, s2))