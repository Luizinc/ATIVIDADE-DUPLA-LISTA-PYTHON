import os
os.system("cls")
quantidade=6
vetor_numero=[]
print('\n digite 6 numeros')

for i in range(quantidade):
    numero=int(input(f'digite seu {i+1}º numero:'))

    if numero% 2 ==0:
        numero=0
        vetor_numero.append(numero)
    else:
        numero=1
        vetor_numero.append(numero)

print(vetor_numero)