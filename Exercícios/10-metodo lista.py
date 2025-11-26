filmsList = ["Inception", "The Shawshank Redemption",
              "The Dark Knight", "Pulp Fiction", "Interstellar"]

# 1 - Tamanho da lista
print(len(filmsList))

# 2 - Recuprerar item da lista pelo indice
print(filmsList.index("Interstellar"))

# 3 - Adicionar um item no fim da lista
filmsList.append("The Lord or the Rings ")
print(filmsList)

# 4 - Ordenar lista
filmsList.sort()
print(filmsList)

# 5 - Copia os itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

# 6 - Remove todos os itens da lista
filmsList.clear()
print(filmsList)