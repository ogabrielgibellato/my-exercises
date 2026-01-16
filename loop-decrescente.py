import os  

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def exibir_nome_do_programa():
    print('Conversão de Crescente para Decrescente\n')

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)

def exibir_menu_principal():
    print('1. Lista Crescente')
    print('2. Lista Decrescente')

def voltar_menu_principal():
    input('\nPressione um botão para voltar ao menu ')
    main()

def escolher_opcao_menu():
    try:
        opcao_escolhida = input('Escolha uma opção: ')
        opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            exibir_subtitulo('Lista Crescente\n')
            print(lista)
            voltar_menu_principal()
        elif opcao_escolhida == 2:
            exibir_subtitulo('Lista Decrescente\n')
            lista_decrescente = sorted(lista, reverse=True)
            print(lista_decrescente)
            voltar_menu_principal()
        else:
            print('Opção inválida! Tente novamente.\n')
            escolher_opcao_menu()
    except ValueError:
        print('Entrada inválida! Por favor, insira um número.\n')
        escolher_opcao_menu()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_menu_principal()
    escolher_opcao_menu()
    # Lógica principal do aplicativo aqui

if __name__ == '__main__':
    main()