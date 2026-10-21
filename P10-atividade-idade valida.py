import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

quantidade = 5
vetor_idade = []
contador = 0

print('=== LEITURA DE IDADES ===')

for i in range(quantidade):
  while True:
    idade = int(input(f'Digite a {i+1}ª idade: '))

    # Validação: precisa estar ENTRE 0 e 120
    if idade >= 0 and idade <= 120:
      print('Idade válida!\n')
      time.sleep(1)
      os.system('cls')
      vetor_idade.append(idade)
      break  # Sai do while e vai para a próxima idade do for
    else:
      print('Idade inválida! Tente novamente.')
      time.sleep(1.5)
      os.system('cls' if os.name == 'nt' else 'clear')

# Conta quantas pessoas têm 18 anos ou mais
for idade in vetor_idade:
  if idade >= 18:
    contador += 1

maxima = max(vetor_idade)
minima = min(vetor_idade)

print('\n=== RESULTADOS ===')
print(f'A maior idade é: {maxima}')
print(f'A menor idade é: {minima}')
print(f'Quantidade de pessoas maiores de idade (18+): {contador}')