# 1 - Função para imprimir um nome completo
def full_name (first_name, last_name):
    print(f"Nome é: {first_name} {last_name}")

full_name("João", "Barros")

# 2 -  Função para somar dois números
def sum_numbers(a,b):
    return a + b

print(f"A soma é {sum_numbers(10,50)}")

# 3 - Função com paramentro default
def adress (country="Brasil"):
    print(f"Eu moro em: {country}")

adress()

# 4 - Função para avaliar um filme
def rate_movie (num_ratings, movie_name):
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme:\n"))
        total += note
    if num_ratings > 0:
        avarage = total / num_ratings
    else:
        avarage = 0
    print(f"Média de avalição do filme {movie_name} é {avarage:.2f}")

rate_movie(2, "Sonic")