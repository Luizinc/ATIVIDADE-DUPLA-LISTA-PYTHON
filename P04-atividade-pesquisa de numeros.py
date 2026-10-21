import os
os.system("cls")
import time

quantidade = 8
vetor_numeros = []


for i in range(quantidade):
    numero = int(input(f'Digite seu {i+1}º número inteiro: '))
    vetor_numeros.append(numero)

os.system('cls')


while True:

    pesquisa = int(input('Digite o número que gostaria de achar: '))

    if pesquisa in vetor_numeros:

        posicao = vetor_numeros.index(pesquisa) + 1
        print(f'Número encontrado na posição: {posicao}')
        break
    else:
        print('Número não encontrado, tente novamente.')
        time.sleep(1)
        os.system('cls')