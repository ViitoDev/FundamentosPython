# 1 - Função para imprimir uma mensagem

def welcome():
    print("Bem-Vindo ao sistema de filmes!")

    # for i in range (10):
    #     welcome()

# 2 - Função para calcular a média de notas 
def calculate_avarage():
    num_ratings = int(input("Digite quantas avaliações deseja fazer para o filme:\n"))
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme:\n"))
        total += note

    if  num_ratings > 0:
        avarage = total / num_ratings
    else:
        avarage = 0

    return avarage

print(f"A média de avaliações é: {calculate_avarage():.2f}")

# 3 - função para cadastrar um filme
def createMovie():
    name = input("Digite o nome do filme:\n")
    yearLaunch = int(input("Digite o ano do filme:\n"))
    noteMovie = float(input("Digite a nota do filme:\n"))
    moviePrice = float(input("Digite o preço do filme:\n"))

    print(f"{name} {yearLaunch} - R$ {moviePrice:.2f}")

createMovie()