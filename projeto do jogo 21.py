'''
criar um projeto de jogo. 
O jogo de cartas blackjack(21), onde consiste em o jogo te dar as cartas e você chegar o mais próximo possivel do número 21. se voce passar o número 21 perde pontos ( você tem 100 pontos, ao chegar a zero você perde. ) se chegar a 21 você ganha pontos, se o jogo tiver cartas com o número maior que o seu voce também perde caso o jogo ultrapasse 21 você ganha. se der empate você nao perderá e nem ganhara.
'''
# passo a passo
# importar a biblioteca tkinter para auxiliar no projeto
# fazer um sistema onde o jogo me dara as cartas de um baralho.( as cartas de um baralho são: As, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13.) o jogo dará 2 cartas e ficara com 2 cartas.
# fazer um sitema de pontuação com o limite de 21 para ganhar tem que chegar o mais próximo ou no limite,se ultrapassar o limite perde, com possibilidade de empate.
# fazer um sistema de ' começar outro jogo? ' [sim/não],caso o jogador falar não. no final o sistema vai somar a pontuação do jogador e do computador para ver quem tem menos pontos, assim, dando a vitória para quem tem maior pontuação.
from tkinter import *
import random

def darcarta():
    return random.choice(cartas)

cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def somar_cartas(mao):
    total = sum(mao)
    # Verificar se há Ás (valor 1) na mão e se o total está abaixo de 12
    if 1 in mao and total <= 11:
        total += 10  # Adicionar 10 para transformar o Ás em 11
    return total

mao_jogador = [darcarta(), darcarta()]
mao_dealer = [darcarta(), darcarta()]

print('Suas cartas:', mao_jogador)
print('Carta do dealer: [?]')

if somar_cartas(mao_dealer) == 21:
    print('Dealer venceu, suas cartas somam 21...')
elif somar_cartas(mao_jogador) == 21:
    print('Jogador venceu, suas cartas somam 21...')
else:
    while True:
        opcao = input('Jogador deseja mais uma carta? [sim/não]: ').lower()
        if opcao == 'sim':
            mao_jogador.append(darcarta())
            print('Suas cartas:', mao_jogador)
            if somar_cartas(mao_jogador) > 21:
                print("Estourou! Jogador perdeu!")
                break
        elif opcao == 'não':
            while somar_cartas(mao_dealer) < 17:
                mao_dealer.append(darcarta())
            print("Mão do dealer:", mao_dealer)
            total_dealer = somar_cartas(mao_dealer)
            total_jogador = somar_cartas(mao_jogador)
            if total_dealer > 21 or total_jogador > total_dealer:
                print("Jogador venceu!")
            elif total_jogador == total_dealer:
                print("Empate!")
            else:
                print("Dealer venceu!")
            break
        else:
            print("Opção inválida! Digite 'sim' ou 'não'.")
