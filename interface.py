import time
import os


# Imprime uma linha ( ========================================== )
def line(tamanho = 42):
    print('=' * tamanho)


# Imprime um cabeçalho com o texto centralizado entre as linhas.
def header(texto):
    line(42)
    print(texto.center(42).upper())
    line(42)


# Imprime um menu com as opções centralizadas.
def menu(*opcoes):
    for i, v in enumerate(opcoes):
        print(f'[{i+1}]. {opcoes[i]}')
    line()


# Limpa o console.
def clearConsole(tempo = 1):
    time.sleep(tempo)
    os.system('clear') # Limpa o console no Linux e macOs
    os.system('cls') # Limpa o console no Windows