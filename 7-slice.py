movieName = "Top Gun"
# string[incio:fim] - indice começa na posição 0 | indice final - 1

# 1 - Buscar toda string a partir da primeira posição
print(movieName[0:])

# 2 - Buscar toda string até a última posição
print(movieName[:7])

# 3 - Buscar toda string da terceira até a última posição
print(movieName[2:])

"""
string[incio:fim:passo]
indice começa na posição 0 | Indice final - 1
passo - determina o incremento. Por padrão esse número é o 1
"""

# 4 - Buscar toda a string de 2 em 2 caracteres
print(movieName[::2])

# 5 - Buscar toda a string nos indices impares
print(movieName[1::2])

# 6 - Inverter uma string de trás para frente 
print(movieName[::-1])