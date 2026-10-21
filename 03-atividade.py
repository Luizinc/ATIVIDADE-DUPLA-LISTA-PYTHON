import os
os.system('cls')

numeros = []
qtd_maiores_10 = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)
    if num > 10:
        qtd_maiores_10 += 1

soma = sum(numeros)

print("\n--- RESULTADOS ---")
print(f"Soma de todos os elementos: {soma}")
print(f"Quantidade de números maiores que 10: {qtd_maiores_10}")