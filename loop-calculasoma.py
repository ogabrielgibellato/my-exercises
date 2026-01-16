import os

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

def exibir_nome_do_programa():
    print('Teste de Numeros Ímpares\n')

def exibir_menu_principal():    
    print('1. Exibir todos os números')
    print('2. Exibir números ímpares\n')

def voltar_menu_principal():
    input('\nPressione um botão para voltar ao menu ')
    main()

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)

def opcao_invalida():
    print('Opção inválida! Tente novamente.\n')
    voltar_menu_principal()

def escolher_opcao_menu():
    try:
        opcao_escolhida = input('Escolha uma opção: ')
        opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            exibir_todos_numeros()
        elif opcao_escolhida == 2:
            exibir_impares()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def exibir_todos_numeros():
    exibir_subtitulo('Todos os Números\n')

    for numero in numeros:
        print(numero)
    voltar_menu_principal()

def exibir_impares():
    exibir_subtitulo('Números Ímpares\n')
    for numero in numeros:
        if int(numero) % 2 != 0:
            print(numero)
    voltar_menu_principal()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_menu_principal()
    escolher_opcao_menu()

if __name__ == '__main__':
    main()