import os

estoque = {'Kafta1,2':  30,
           'Hamburguer':  50,
           'Coca-Cola':  100,}

def exibir_nome_do_programa():
    print('Espetinhos Curitiba Estoque\n')

def voltar_menu_principal():
    input('\nPressione um botão para voltar ao menu ')
    main()

def exibir_menu_principal():
    print('1. Verificar Estoque')
    print('2. Adicionar Itens ao Estoque')
    # A função 3 será responsável por ALTERAR OU REMOVER
    print('3. Alterar ou Remover Itens do Estoque')
    print('4. Sair\n')

def escolher_opcao_menu():
    opcao = input('Escolha uma opção: ')
   
    if opcao == '1':
        verificar_estoque()
    elif opcao == '2':
        adicionar_estoque()
    elif opcao == '3':
        # Função única para Alterar/Remover
        alterar_ou_remover_estoque()
    elif opcao == '4':
        finalizar_app() # Agora a opção 4 é Sair
    else:
        opcao_invalida()

def verificar_estoque():
    print('\nEstoque Atual:\n')
    for item, quantidade in estoque.items():
        print(f' - {item.ljust(20)} | Quantidade: {quantidade}')
    voltar_menu_principal()      

def adicionar_estoque():
    item = input('Digite o nome do item que deseja adicionar ao estoque: ')
    quantidade = int(input('Digite a quantidade a ser adicionada: '))
   
    if item in estoque:
        estoque[item] += quantidade
    else:
        estoque[item] = quantidade
   
    print(f'Item {item} adicionado com sucesso. Nova quantidade: {estoque[item]}')
    voltar_menu_principal()

def alterar_ou_remover_estoque():
    print('\n--- Alterar ou Remover Item ---')
    item_desejado = input('Digite o nome do item que deseja alterar ou remover: ').strip()
   
    # 1. Verificar se o item existe
    if item_desejado in estoque:
        quantidade_atual = estoque[item_desejado]
        print(f"\nItem encontrado! Quantidade atual: {quantidade_atual}")
        print("\nO que deseja fazer?")
        print("1 - Alterar a quantidade")
        print("2 - Remover item completamente")
        print("3 - Cancelar")
       
        escolha = input("Escolha uma opção (1-3): ").strip()

        if escolha == '1':
            # Lógica de Alterar a Quantidade
            try:
                nova_quantidade = int(input(f'Digite a NOVA quantidade de {item_desejado}: '))
                if nova_quantidade >= 0:
                    estoque[item_desejado] = nova_quantidade
                    print(f'\nSUCESSO: Quantidade de {item_desejado} alterada para {nova_quantidade}.')
                else:
                    print('\nERRO: A quantidade não pode ser negativa.')
            except ValueError:
                print('\nERRO: Por favor, digite um número inteiro válido.')
               
        elif escolha == '2':
            # Lógica de Remover Item (usando 'del')
            confirmacao = input(f'Tem certeza que deseja remover {item_desejado} do estoque? (s/n): ').lower()
            if confirmacao == 's':
                del estoque[item_desejado]
                print(f'\nSUCESSO: Item {item_desejado} foi removido do estoque.')
            else:
                print('\nOperação cancelada.')
               
        elif escolha == '3':
            print('\nOperação cancelada.')
           
        else:
            print('\nEscolha inválida.')
           
    else:
        print(f"\nERRO: Item '{item_desejado}' não encontrado no estoque.")
       
    voltar_menu_principal()

def finalizar_app():
    print('Finalizando o APP...')  

def opcao_invalida():
    print('\nOpção inválida. Tente novamente.\n')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_menu_principal()
    escolher_opcao_menu()
    # Lógica principal do aplicativo aqui

if __name__ == '__main__':
    main()