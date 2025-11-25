# # Informações do filme
# name = input("Digite o nome do filme:\n")
# yearRelease = int(input("Digite o ano de lançamento:\n"))
# rating = float(input("Digite a nota de avaliação do filme:\n"))

# # Verifica se o filme é recomendado
# if rating > 8.0 and yearRelease > 2015:
#     print(f"O filme {name} é bom!")
# else:
#     print(f"O filme {name} ainda não tem nota maior que 8")

num1 = float(input("Digite o 1° número:\n"))
num2 = float(input("Digite o 2° número:\n"))
operation = input("Digite a operação a ser realizada: ( + | - | * | /  )\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro, divisão por 0")
        result = 0
else:
    print("Operação inválida")
    result = 0

print(f"Seu resultado é {result:.2f}")