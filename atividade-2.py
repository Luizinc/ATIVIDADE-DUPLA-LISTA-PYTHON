import os
os.system('cls')
import time
vetor_temperatura=[]
quantidade=7
for i in range (quantidade):
    ('\n==TEMPERATURA==')
    temperatura=int(input('digite a temperatura de hoje:'))
    vetor_temperatura.append(temperatura)

print('==RESULTADOS==')

print(f'temperatura durante a semana {vetor_temperatura}')
print(f'temperatura maxima {max(vetor_temperatura)}')
print(f'temperatura maxima {min(vetor_temperatura)}')
