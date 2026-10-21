import os
os.system('cls')

quantidade=7
vetor_temperatura=[]
for i in range(quantidade):
    temperatura=(int(input(f'digite a {i+1}º temperatura: ')))
    vetor_temperatura.append(temperatura)
    
print('\n===RESULTADOS===')
maxima= max (vetor_temperatura)
minima= min (vetor_temperatura)

print(f'temperatura durante a semana:{vetor_temperatura} ')
print(f'maior temperatura:{maxima} ')
print(f'menor temperatura:{minima} ')