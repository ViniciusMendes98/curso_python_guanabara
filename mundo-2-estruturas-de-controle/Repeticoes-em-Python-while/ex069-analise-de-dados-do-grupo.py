#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.   
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.
cont18 = contH = contM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    while sexo not in 'MF':
        print('Digite apenas M ou F.')
        sexo = input('Sexo [M/F]: ').strip().upper()
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        contH += 1
    if sexo == 'F' and idade < 20:
        contM20 += 1
    resp = input('Deseja continuar? [S/N]: ').strip().upper()
    while resp not in 'SN':
        print('Digite apenas S ou N.')
        resp = input('Deseja continuar? [S/N]: ').strip().upper()
    if resp == 'N':
        break
print(f'Pessoas com mais de 18 anos: {cont18}')
print(f'Homens cadastrados: {contH}')
print(f'Mulheres com menos de 20 anos: {contM20}')