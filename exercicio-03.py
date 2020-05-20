# Exercício 3

#Tomando como base a Tabela 1, construa um gráfico de barras horizontal
#com os dados da distribuição da população masculina.

import matplotlib.pyplot as plt

# Inserindo as séries
idade = [ "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34",
         "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69",
         "70-74", "75-79", "80-84", "85-89", "90-94", "95-99", "> 100" ]

masculino = [ 7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664, 6320568, 5692014, 4834995,
             3902344, 3041035, 2224065, 1667372, 1090517, 668623, 310759, 114964, 31529, 7247 ]

ano = [x for x in range(len(idade))]

# Definindo o tamanho da figura do gráfico
plt.figure( figsize=(10, 8) )

# Definindo as barras (horizontal, centralizado, cor azul, borda preta com espessura da linha igual a 1)
plt.barh(ano, masculino, align='center', color='blue', linewidth=1, edgecolor='black')

# Definindo o eixo x
plt.xticks([ 0, 2250000, 4500000, 6750000, 9000000 ],
           [ "0", "2,25 milhões", "4,5 milhões", "6,75 milhões", "9 milhões" ] )

# Definindo o eixo y
plt.yticks(ano, idade)

# Definindo o título do gráfico
plt.title("Distribuição da população masculina em 2010")

# Definido os rótulos dos eixos
plt.xlabel("População")
plt.ylabel("Idade")

# Inserindo um grid
plt.grid(b=True, color='gray', linestyle='--', linewidth=0.5);

# Apresentar o gráfico
plt.show()