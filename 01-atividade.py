import os
os.system('cls')


numeros = []


for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)


print("\nOrdem digitada:", *numeros)
print("Ordem inversa:", *numeros[::-1])