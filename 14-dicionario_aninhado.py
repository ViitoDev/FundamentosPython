filmsDict = {
    "Inception": {
        "yearRealse": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "Interstellar": {
        "yearRealse": 2014,
        "imdbRating": 8.6,
        "genre": ["Sci-fi", "Drama"]
    },
    "The Dark Knight": {
        "yearRealse": 2008,
        "imdbRating": 9.0,
        "genre": ["Action", "Drama", "Crime"]
    }
}


print(filmsDict)

# 1 - Buscar uma informação dentro de um dicionário aninhado
print(filmsDict["Interstellar"]["genre"])

# 2 - Adicionar um item
filmsDict["Inception"]["Director"] = "Christopher Nolan"
print(filmsDict["Inception"])

# 3 - Excluir um dicionário
del filmsDict["The Dark Knight"]
print(filmsDict)