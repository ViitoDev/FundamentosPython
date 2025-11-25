# Lista de filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - iterando valores de uma lista de filmes usando while
index = 0
while index < len(moviesList):
    print(moviesList[index])
    index += 1

# 2 - Quando a condição for atendida, o loop será encerrado
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        break 
    print(moviesList[index])
    index += 1

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        index += 1
        continue 
    print(moviesList[index])
    index += 1

# 4 - Avaliação de filmes com while
movieName = input("Digite o nome do filme:\n")
movieRate = float(input("Digite quantas avaliações deseja fazer:\n"))

total = 0
count = 0

while count < movieRate:
    note = float(input("Digite a nota para o filme:\n"))
    total += note
    count += 1
    
if movieRate > 0:
    avarage = total / movieRate
else:
    avarage = 0

print(f"A média de avaliação do filme {movieName} é: {avarage:.2f}")