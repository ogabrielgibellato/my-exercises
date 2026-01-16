import os

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
nomes = ['João', 'Maria', 'José', 'Ana', 'Pedro', 'Lucas', 'Paula', 'Carla', 'Rafael', 'Fernanda']
anos_nascimento = ['1990', '1985', '2000', '1995', '1988', '1992', '1993', '1987', '1986', '1991']

def exibir_nome_do_programa():
    print('\nPrimeiro Exercício\n')

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)
   

def menu_principal():
    print('1. Visualizar Numeros')
    print('2. Visualizar Nomes')
    print('3. Visualizar Anos de Nascimento')

def escolher_opcao():
    opcao = input('\nEscolha uma opção: ')
    if opcao == '1':
        visualizar_numeros()
    elif opcao == '2':
        visualizar_nomes()
    elif opcao == '3':
        visualizar_anos_nascimento()
    else:
        print('Opção inválida! Tente novamente.\n')
        voltar_ao_menu()

def voltar_ao_menu():
    input('\nPressione Enter para voltar ao menu principal...')
    main()

def visualizar_numeros():
    exibir_subtitulo('Numeros:')

    for numero in numeros:
        print(f' .{numero}')
   
    voltar_ao_menu()

def visualizar_nomes():
    exibir_subtitulo('Nomes:')
   
    for nome in nomes:
        print(f' .{nome}')
   
    voltar_ao_menu()

def visualizar_anos_nascimento():
    exibir_subtitulo('Anos de Nascimento:')

    for ano in anos_nascimento:
        print(f' .{ano}')
   
    voltar_ao_menu()

def main():
    exibir_nome_do_programa()
    menu_principal()
    escolher_opcao()

if __name__ == '__main__':
    main()