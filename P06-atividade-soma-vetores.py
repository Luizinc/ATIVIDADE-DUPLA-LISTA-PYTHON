import os
os.system('cls')

vetor_principal=[]
vetor_C=[]
quantidade=10

print('\n digite 10 numeros')
for i in range(quantidade):

    numero=int(input(f'digite seu {i+1}º numero:'))
    vetor_principal.append(numero)
vetor_A=vetor_principal[5:]
vetor_B=vetor_principal[:5]

for i in range(5):
    vetor_soma = vetor_A[i] + vetor_B[i]
    vetor_C.append(vetor_soma)

print(vetor_C)