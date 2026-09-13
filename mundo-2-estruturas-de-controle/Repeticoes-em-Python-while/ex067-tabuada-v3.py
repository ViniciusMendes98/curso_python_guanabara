#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Digite um número para ver a sua tabuada (negativo para parar): '))
    if n < 0:
        break
    print('-' * 30)
    print(f'Tabuada do {n}:')
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print('-' * 30)
print('PROGRAMA DE TABUADA ENCERRADO!')