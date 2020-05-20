# Exercício 2

# A Tabela 1, extraída do portal do IBGE, apresenta a distribuição da
# população por sexo, segundo os grupos de idade no Brasil, para o ano de 2010. Com
# base nesta tabela, construa um gráfico de barras vertical com os dados da distribuição da
# população feminina.

import matplotlib.pyplot as plt

idade = [ "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34",
         "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69",
         "70-74", "75-79", "80-84", "85-89", "90-94", "95-99", "> 100" ]

feminino = [ 6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796, 6141338,
           5305407, 4373877, 3468085, 2616745, 2074264, 1472930, 998349, 508724, 211594, 66806, 16989 ]

x_pos = [ x for x in range( len(idade) ) ]

# Definindo o tamanho da figura do gráfico
plt.figure( figsize=(10, 8) )

# Definindo as barras (vertical, centralizado, cor rosa, borda preta com espessura da linha igual a 1)
plt.bar(x_pos, feminino, align='center',
        color='pink', linewidth=1, edgecolor='black')

plt.xticks(x_pos, idade, rotation=45)

# Definindo o eixo y
plt.yticks([ 0, 2250000, 4500000, 6750000, 9000000 ],
           [ "0", "2,25 milhões", "4,5 milhões", "6,75 milhões", "9 milhões" ] )

# Definindo o título do gráfico
plt.title("Distribuição da população feminina em 2010")

# Definido os rótulos dos eixos
plt.xlabel("Idade")
plt.ylabel("População")

# Inserindo um grid
plt.grid(b=True, color='gray', linestyle='--', linewidth=0.5);

# Apresentar o gráfico
plt.show()