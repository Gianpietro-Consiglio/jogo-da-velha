import sys
import random
import time


def linha():
    print('')


repetidos = []
tabuleiro = []
lista = []
aviso = []
c = ''
g = ''
for x in range(0, 10):
    tabuleiro.append(x)
    
soma = 0
for _ in range(0, 3):
    soma += 3
    print(tabuleiro[soma - 3], tabuleiro[soma - 2], tabuleiro[soma - 1])
linha()
while True:
    a = ''
    if len(repetidos) == 9:
        print('VELHA')
        sys.exit()
    escolha = int(input('Qual posição jogar? '))
    if escolha in repetidos:
        while True:
            escolha = int(input('Outra posição: '))
            if escolha not in repetidos:
                repetidos.append(escolha)
                break
    else:
        repetidos.append(escolha)

    a = random.randint(0, 8)
    if a in repetidos:
        tempo = time.time()
        while True:
            if len(repetidos) == 9:
                print('VELHA')
                sys.exit()
            a = random.randint(0, 8)
            if a not in repetidos:
                repetidos.append(a)
                break
            #else:
                #if tempo > 100000:
                   # print('Limite expirado!')
                    #time.sleep(2)
                   # break
    else:
        repetidos.append(a)
              

    linha()
    soma = 0
    for c in tabuleiro:
        if c == escolha:
            tabuleiro.remove(c)
            tabuleiro.insert(c, 'X')

        elif c == a:
            tabuleiro.remove(c)
            tabuleiro.insert(c, 'O')
    soma = 0
    for _ in range(0, 3):
        soma += 3
        print(tabuleiro[soma - 3], tabuleiro[soma - 2], tabuleiro[soma - 1])
    print(f'COMPUTADOR JOGOU NA POSIÇÃO -> [{a}]')
    linha()

    def validar(f, h, j):
        if tabuleiro[f] == 'X' and tabuleiro[h] == 'X' and tabuleiro[j] == 'X':
            print('VOCÊ GANHOU!')
            time.sleep(3)
            sys.exit()

        elif tabuleiro[f] == 'O' and tabuleiro[h] == 'O' and tabuleiro[j] == 'O':
            print('COMPUTADOR GANHOU!')
            time.sleep(3)
            sys.exit()

    validar(0, 1, 2)
    validar(3, 4, 5)
    validar(6, 7, 8)
    validar(0, 3, 6)
    validar(1, 4, 7)
    validar(2, 5, 8)
    validar(0, 4, 8)
    validar(2, 4, 6)
