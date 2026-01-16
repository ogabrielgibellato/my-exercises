import os

pessoas = [{'nome':'Adriano','idade:':'17', 'cidade': 'Sao Paulo'},
                {'nome':'Bernarda','idade:':'105', 'cidade': 'Itapipoca'},
                {'nome':'Jose Augusto','idade:':'45', 'cidade': 'Ponta Grossa'}]

def exibir_nome_do_programa():
    print('Gerenciamento de Pessoas\n')

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)

def voltar_menu_principal():
    input('\nPressione um botão para voltar ao menu ')
    main()

def exibir_menu_principal():
    print('1. Cadastrar Pessoa')
    print('2. Listar Pessoas')
    print('3. Sair\n')

def escolher_opcao_menu():
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        cadastrar_pessoa()
    elif opcao == '2':
        listar_pessoas()
    elif opcao == '3':
        finalizar_app()
    else:
        opcao_invalida()

def cadastrar_pessoa():    
    exibir_subtitulo('Cadastro de Pessoa')
   
    nome_da_pessoa = input('Nome da Pessoa: ')
    idade = input(f'Idade de {nome_da_pessoa}: ')
    cidade = input(f'Cidade de {nome_da_pessoa}: ')
   
    dados_da_pessoa = {'nome': nome_da_pessoa,
                       'idade': idade,
                       'cidade': cidade}
    pessoas.append(dados_da_pessoa)
   
    print(f'\nPessoa {nome_da_pessoa} cadastrada com sucesso!')
    voltar_menu_principal()

def listar_pessoas():  
    exibir_subtitulo('Lista de Pessoas')

    print('Nome'.ljust(20), '|', 'Idade'.ljust(10), '|', 'Cidade')
    print('-' * 50 + '\n')
    for pessoa in pessoas:
        nome = pessoa['nome']
        idade = pessoa['idade']
        cidade = pessoa['cidade']
        print(f' - {nome.ljust(18)} | {idade.ljust(8)} | {cidade}')

    voltar_menu_principal()

def opcao_invalida():
    print('Opção inválida! Tente novamente.\n')
    voltar_menu_principal()

def finalizar_app():
    exibir_subtitulo('Finalizando o APP ')
    os._exit(0)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_menu_principal()
    escolher_opcao_menu()
    # Lógica principal do aplicativo aqui

if __name__ == '__main__':
    main()