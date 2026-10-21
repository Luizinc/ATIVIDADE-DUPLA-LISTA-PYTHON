import os
os.system('cls')

notas = []

for i in range(5):
    nota= float(input(f'digite a {i+1}ª nota: '))
    notas.append(nota)

media = sum(notas)/len(notas)
acima_da_media = sum(1 for nota in notas if nota > media)

print(f'=====RESULTADOS=====')
print("Notas digitadas:", *[f"{n:.1f}" for n in notas])
print(f"Média da turma: {media:.2f}")
print(f"Quantidade de notas acima da média: {acima_da_media}")