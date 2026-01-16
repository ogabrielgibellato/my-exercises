import os

quadrados = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def exibir_nome_do_programa():  
    print('Elevações ao Quadrado\n')

def exibir_menu_principal():
    print('1. Escolha um numero de 1 a 5 para ver seu quadrado:')
    print('2. Sair\n')

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)

def voltar_menu_principal():
    input('\nPressione um botão para voltar ao menu ')
    main()

def finalizar_app():
    exibir_subtitulo('Finalizando o APP ')
    os._exit(0)

def escolher_opcao_menu():
    try:
        opcao_escolhida = input('Escolha uma opção: ')
        opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida in quadrados:
            print(f'O quadrado de {opcao_escolhida} é {quadrados[opcao_escolhida]}.\n')
        elif opcao_escolhida == 2:
            print('Finalizando o APP...')
        else:
            print('Opção inválida. Tente novamente.\n')
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.\n')

    voltar_menu_principal()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_menu_principal()
    escolher_opcao_menu()
    # Lógica principal do aplicativo aqui

if __name__ == '__main__':
    main()