nomes = []
salarios = []

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º funcionário: ")
    salario = float(input(f"Digite o salário de {nome}: R$ "))
    nomes.append(nome)
    salarios.append(salario)


maior_salario = max(salarios)
indice_maior = salarios.index(maior_salario)
nome_maior = nomes[indice_maior]


acima_2000 = sum(1 for salario in salarios if salario > 2000)

print("\n--- RESULTADOS ---")
print(f"Funcionário com maior salário: {nome_maior} (R$ {maior_salario:.2f})")
print(f"Quantidade que ganha acima de R$ 2.000,00: {acima_2000}")