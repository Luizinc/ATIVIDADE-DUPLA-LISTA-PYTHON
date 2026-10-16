import os

vetor_numeros = []
QUANTIDADE_NUMEROS = 5

os.system('cls' if os.name == 'nt' else 'clear')

print('== LEITURA DOS NÚMEROS ==')


for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f'Digite o {i+1}º número inteiro: '))
    vetor_numeros.append(numero)

print('\n== ORDEM DIGITADA ==')
print(f'ORDEM PADRAO {vetor_numeros}')
print(f'ORDEM INVERSA {vetor_numeros[::-1]}')
