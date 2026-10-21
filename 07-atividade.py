import os
os.system('cls')

print(f'====OLÁ PEQUENO GAFANHOTO====')

vetor_origem = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor_origem.append(num)


vetor_positivos = [num for num in vetor_origem if num > 0]
qtd_copiados = len(vetor_positivos)

print("\n--- RESULTADOS ---")
if qtd_copiados > 0:
    print("Vetor de números positivos:", *vetor_positivos)
else:
    print("Nenhum número positivo foi digitado.")

print(f"Total de elementos copiados: {qtd_copiados}")