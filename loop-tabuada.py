import os

numero = []

def exibir_nome_do_programa():
    print('Sistema de Tabuadas')

def exibir_subtitulo(subtitulo):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\n{subtitulo}')

def voltar_menu_principal():
    input('\nPressione Enter para voltar ao menu principal...')
    main()

def exibir_menu_principal():
    try:
        # Pede, recebe, converte para int e RETORNA o valor
        numero_digitado = int(input('\nDigite um número para ver a tabuada: '))
        return numero_digitado
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        # Retorna 0 ou chama a função novamente para garantir uma entrada válida
        return 0

def exibir_tabuada(numero):
    """
    Exibe a tabuada de um número fornecido, de 1 até 10.

    Args:
        numero (int): O número do qual a tabuada será calculada.
    """
    print(f"\nTabuada do {numero}")
    # ESTA LINHA GERA O TÍTULO DA TABUADA
   
    # O loop 'range(1, 11)' gera números de 1 até 10 (o 11 é exclusivo)
    for i in range(1, 11):
        resultado = numero * i
        # Formata a saída para mostrar a operação e o resultado
        print(f"{numero} x {i:2} = {resultado}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    # 1. CAPTURA O NÚMERO: A variável 'num' armazena o valor RETORNADO.
    num = exibir_menu_principal()
   

    # 2. LÓGICA DE EXIBIÇÃO: Verifica se a entrada foi válida (não é 0)
    if num != 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        # 3. CHAMA A TABUADA: Passa o número capturado como ARGUMENTO.
        exibir_tabuada(num)
       
    # 4. VOLTA AO MENU: Permite que o usuário veja o resultado antes de sair.
    voltar_menu_principal()

if __name__ == '__main__':
    main()