# Exemplo 1:
# primeiroNome = input("Digite o nome: ")
# segundoNome = input("Digite o sobrenome: \n")

# nomeFormatado = f"{segundoNome} {primeiroNome}"
# print(nomeFormatado)

# Exemplo 2:
# texto = "Python é muito interessante"
# palavras = texto.split()
# textoInvertido = " ".join(palavras[::-1])
# print(textoInvertido)

# Exemplo 3
texto1 = "arara"
texto2 = "ovo"

# Remove espaço e deixe nome em minúsculo
texto1_format = texto1.lower().replace(" ", "")
texto1_format = texto2.lower().replace(" ", "")

# Verifica se texto original é igual ao seu reverso
palindromo1 = texto1_format == texto1[::-1]
palindromo2 = texto1_format == texto1[::-1]

print(palindromo1)
print(palindromo2)