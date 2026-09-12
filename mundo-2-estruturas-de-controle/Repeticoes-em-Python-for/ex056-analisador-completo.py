#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo  
#Qual é o nome do homem mais velho
#Quantas mulheres têm menos de 20 anos
soma_idade = 0
homem_mais_velho = 0
maior_idade_homem = 0
mulheres_menos_20 = 0
nomes_homens = 0
for i in range(4):
    print(f'----- {i+1}ª PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    soma_idade += idade
    if sexo == 'M':
        nomes_homens += 1
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            homem_mais_velho = nome
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
media_idade = soma_idade / 4
print(f'\nA média de idade do grupo é de {media_idade:.1f} anos.')
print(f'O homem mais velho é {homem_mais_velho} com {maior_idade_homem} anos.')
print(f'Há {mulheres_menos_20} mulher(es) com menos de 20 anos.')