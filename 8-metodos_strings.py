movieName = "Top Gun"

movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura
muito consagrado na indústria
"""

print(movieName.upper()) # Tudo maiusculo
print(movieName.lower()) # Tudo minusculo
print(movieName.capitalize()) # Primeira letra maiúscula
print(movieName.title()) # Primeira letra maiuscula
print(movieName.center(10, "-")) # Retorna string centralizada com caractere de preenchimento 
print(movieName.find("u")) # Retorna a posição de um determinado caractere
print(movieName.find("o")) # Conta caracteres
print(movieName.replace("Top", "Matrix")) # Altera um elemento por outro
print(movieDescription.split(","))