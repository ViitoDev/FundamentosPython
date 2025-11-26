# 1 - Soma de números
def sum (*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é igual a {sum_total}")

sum(7,9,2)

# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("Lista de cursos:")
presentation(name="Python", cathegory="Back-end", level="Iniciante")
presentation(name="Visão computacional", cathegory="AI", level="Avançado")
presentation(name="Dashboards com dash", cathegory="data-science", level="Intermediário")