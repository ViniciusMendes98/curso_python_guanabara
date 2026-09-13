#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor = int(input('Qual o valor a ser sacado? R$'))
cedula = 50
while True:
    quantidade = valor // cedula
    if quantidade > 0:
        print(f'Total de {quantidade} cédulas de R${cedula}')
        valor %= cedula
    if valor == 0:
        break
    if cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1