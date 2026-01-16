import os

pessoas = [{'nome':'Adriano','idade':'17', 'cidade': 'Sao Paulo'},
                {'nome':'Bernarda','idade':'105', 'cidade': 'Itapipoca'},
                {'nome':'Jose Augusto','idade':'45', 'cidade': 'Ponta Grossa'}]

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
    print('3. Alterar Dados')
    print('4. Sair\n')

def escolher_opcao_menu():
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        cadastrar_pessoa()
    elif opcao == '2':
        listar_pessoas()
    elif opcao == '3':
        alterar_dados()
    elif opcao == '4':
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

    print('Nome'.ljust(20), '|', 'Idade'.ljust(10), '|', 'Cidade'.ljust(15), '|', 'Profissão')
    print('-' * 50 + '\n')
    for pessoa in pessoas:
        nome = pessoa['nome']
        idade = pessoa['idade']
        cidade = pessoa['cidade']
        profissao = pessoa.get('profissao', '(não cadastrada)')
        print(f' - {nome.ljust(18)} | {idade.ljust(8)} | {cidade.ljust(15)}  | {profissao}')

    voltar_menu_principal()

def alterar_dados():
    exibir_subtitulo('Alterar Dados da Pessoa')
   
    nome_da_pessoa = input('Digite o nome da pessoa que deseja alterar: ')
    for pessoa in pessoas:
        if pessoa['nome'].lower() == nome_da_pessoa.lower():
            # mostra os dados atuais
            idade_atual = pessoa.get('idade', '')
            cidade_atual = pessoa.get('cidade', '')
            profissao_atual = pessoa.get('profissao', '(não cadastrada)')
            print(f"\nDados atuais: Idade: {idade_atual} | Cidade: {cidade_atual} | Profissão: {profissao_atual}\n")

            # pergunta o que o usuário quer alterar
            print("O que deseja alterar?")
            print("1 - Idade")
            print("2 - Cidade")
            print("3 - Adicionar/Editar Profissão")
            print("4 - Cancelar")
            escolha = input("Escolha uma opção (1-4): ").strip()

            if escolha == '1':
                nova_idade = input(f'Nova idade de {pessoa["nome"]} (pressione Enter para manter {idade_atual}): ').strip()
                if nova_idade != '':
                    pessoa['idade'] = nova_idade
                    print(f'Idade atualizada para {nova_idade}.')
                else:
                    print('Idade mantida.')

            elif escolha == '2':
                nova_cidade = input(f'Nova cidade de {pessoa["nome"]} (pressione Enter para manter {cidade_atual}): ').strip()
                if nova_cidade != '':
                    pessoa['cidade'] = nova_cidade
                    print(f'Cidade atualizada para {nova_cidade}.')
                else:
                    print('Cidade mantida.')

            elif escolha == '3':
                nova_profissao = input(f'Profissão de {pessoa["nome"]} (pressione Enter para manter {profissao_atual}): ').strip()
                if nova_profissao != '':
                    pessoa['profissao'] = nova_profissao
                    print(f'Profissão atualizada para {nova_profissao}.')
                else:
                    # se não tinha profissão e o usuário apertou Enter, não cria nada novo
                    if 'profissao' in pessoa:
                        print('Profissão mantida.')
                    else:
                        print('Nenhuma profissão cadastrada.')

            else:
                print('Operação cancelada ou escolha inválida.')

            print(f'\nDados de {pessoa["nome"]} atualizados com sucesso!')
            break
    else:
        print(f'\nPessoa {nome_da_pessoa} não encontrada.')

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