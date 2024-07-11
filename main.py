import random
from interface import *

# Função para gerar a senha
def generatePassword(tiposEscolhidos, tamanhoSenha):
    senha = []  # Lista para armazenar os caracteres da senha
    listaCaracteres = [  # Lista de listas contendo os caracteres possíveis para a senha
        ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],  # Letras minúsculas
        ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],  # Letras maiúsculas
        ['!', '@', '#', '$', '%', '&', '*', '+', '=', '?'],  # Caracteres especiais
        [1,2,3,4,5,6,7,8,9,0]  # Números
    ]

    # Loop até que a senha atinja o tamanho desejado
    while len(senha) < int(tamanhoSenha):
        if '1' in tiposEscolhidos:  # Se o usuário escolheu números
            senha.append(str(random.choice(listaCaracteres[3])))  # Adiciona um número à senha
        if '2' in tiposEscolhidos:  # Se o usuário escolheu letras maiúsculas
            senha.append(random.choice(listaCaracteres[1]))  # Adiciona uma letra maiúscula à senha
        if '3' in tiposEscolhidos:  # Se o usuário escolheu letras minúsculas
            senha.append(str(random.choice(listaCaracteres[0])))  # Adiciona uma letra minúscula à senha
        if '4' in tiposEscolhidos:  # Se o usuário escolheu caracteres especiais
            senha.append(random.choice(listaCaracteres[2]))  # Adiciona um caractere especial à senha

    random.shuffle(senha)  # Embaralha os caracteres da senha para aumentar a segurança
    
    return ''.join(senha)  # Retorna a senha como uma string

# Função para obter a escolha do usuário
def getUserChoice():
    header('GERADOR DE SENHA')  # Exibe o cabeçalho
    menu('Números',  # Exibe o menu de opções
         'Letras Maiúsculas',
         'Letras Minúsculas',
         'Caracteres Especiais',
         'FINALIZAR')
    
    tiposEscolhidos = []  # Lista para armazenar os tipos de caracteres escolhidos pelo usuário
    opcoes = {'1': 'Números', '2': 'Letras Maiúsculas', '3': 'Letras Minúsculas', '4': 'Caracteres Especiais', '5': 'FINALIZAR'}

    while True:
        caracterEscolhido = input('DIGITE O NÚMERO DO CARACTER QUE DESEJA: ')  # Pede ao usuário para escolher um tipo de caractere
        if caracterEscolhido not in opcoes:  # Verifica se a escolha é válida
            print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')  # Mensagem de erro para escolha inválida
            clearConsole(0.75)  # Limpa o console após 0,75 segundos
            continue
        
        if caracterEscolhido == '5':  # Se o usuário escolheu finalizar
            line()  # Exibe uma linha no console
            tamanhoSenha = input('DIGITE O TAMANHO DA SENHA: ')  # Pede ao usuário para digitar o tamanho da senha
            print('CARREGANDO', end='')  # Mensagem de carregamento
            for i in range(3):
                time.sleep(0.45)
                print('.', end='')  # Exibe pontos de carregamento
            break  # Sai do loop
        else:
            tiposEscolhidos.append(caracterEscolhido)  # Adiciona a escolha do usuário à lista
    
    return tiposEscolhidos, tamanhoSenha  # Retorna os tipos de caracteres escolhidos e o tamanho da senha

# Função principal para gerar a senha
def getPassword():
    tiposEscolhidos, tamanhoSenha = getUserChoice()  # Obtém a escolha do usuário
    senha = generatePassword(tiposEscolhidos, tamanhoSenha)  # Gera a senha com base na escolha do usuário
    
    clearConsole()  # Limpa o console
    line()  # Exibe uma linha no console
    print('SENHA GERADA ALEATORIAMENTE'.center(42))  # Exibe mensagem centralizada
    print(f'{senha}'.center(42))  # Exibe a senha centralizada
    line()  # Exibe uma linha no console

if __name__ == "__main__":
    getPassword()  # Chama a função principal para gerar a senha se o script for executado diretamente
