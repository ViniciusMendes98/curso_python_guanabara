#Melhore o jogo do ex028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

computador = randint(0, 10)
palpites = 0
jogador = -1
while jogador != computador:
    jogador = int(input('Digite um número entre 0 e 10: '))
    if jogador < 0 or jogador > 10:
        print('Número inválido!')
    else:
        palpites += 1
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
        else:
            print(f'Parabéns! Você acertou em {palpites} palpites.')