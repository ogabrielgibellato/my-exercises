import os

items_vendidos = []

def exibir_nome_do_programa():
    '''Essa função é responsável por exibir o nome do programa'''
    texto = 'Verificação de Vendas'
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha + '\n')

def exibir_subtitulo(texto):

    '''Essa função é responsável por exibir subtítulos no programa
   
    Inputs:
        - Texto do subtítulo
   
    Outputs:
        - Subtítulo formatado com linhas de asteriscos acima e abaixo do texto
   
    '''

def exibir_menu_principal():
    '''Essa função é responsável por exibir o menu principal do programa

    Inputs: Solicita o nome do item vendido e sua quantidade
   
    Outputs:
        - Opções sendo: Cadastrar Restaurante, Listar Restaurantes, Ativar Restaurante e Sair
   
    '''
    print('1. Insira os itens vendidos e a quantidade')

    try:
        item_vendido = input('Item vendido: ')
        quantidade_vendida = int(input('Quantidade vendida: '))
        items_vendidos.append({'item': item_vendido, 'quantidade': quantidade_vendida})
        print(f'\nSucesso: {quantidade_vendida} unidades de "{item_vendido}" registradas!')

        escolha = input('\nDeseja cadastrar outro item? (S/N): ').upper()
           
        if escolha == 'S':
                main() # Reinicia o ciclo para novo cadastro
        elif escolha == 'N':
                mostrar_item_mais_vendido()
        else:
                finalizar_app()

    except ValueError:
        print('\nErro: A quantidade deve ser um número inteiro.')
        input('Pressione qualquer tecla para tentar novamente...')
        main()

def mostrar_item_mais_vendido():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_subtitulo('Campeão de Vendas')
    if not items_vendidos:
        return

    # 1. Agrupar quantidades totais por item
    totais = {}
    for registro in items_vendidos:
        item = registro['item']
        quantidade = registro['quantidade']
        totais[item] = totais.get(item, 0) + quantidade

    # 2. Descobrir qual é a MAIOR quantidade vendida
    maior_quantidade = max(totais.values())

    # 3. Criar uma lista com todos os itens que atingiram essa quantidade (filtro)
    campeoes = [item for item, qtd in totais.items() if qtd == maior_quantidade]

    # 4. Exibição inteligente
    if len(campeoes) > 1:
        print(f'\n🤝 Tivemos um EMPATE entre os itens mais vendidos!')
        print(f'📊 Cada um vendeu um total de: {maior_quantidade} unidades.')
        print('Os itens campeões são:')
        for item in campeoes:
            print(f'  -> {item}')
    else:
        print(f'\n🏆 O item mais vendido foi: {campeoes[0]}')
        print(f'📊 Total de vendas: {maior_quantidade} unidades.')

def finalizar_app():
    '''Essa função é responsável por finalizar o programa'''
    exibir_subtitulo('Finalizando o APP ')
    os._exit(0)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_menu_principal()
    # Lógica principal do aplicativo aqui

if __name__ == '__main__':
    main()