import os

# Lista de números e textos mistos (para simular dados sujos)
numeros = [1, 2, 3, '4', 'cinco', 6, 7, 'oito', 9, '10', 11, 12, 'treze', 14, 15, 16, 'dezessete', 18, 19, 'vinte']

def exibir_nome_do_programa():
    print('Programa de Soma de Números\n')
    input('Pressione um botão para continuar...')

def voltar_menu_principal():
    input('\nPressione um botão para voltar ao menu principal...')
    main()

def exibir_soma():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('## ➕ Calculadora de Soma Inteligente')
   
    soma = 0
   
    for elemento in numeros:
        try:
            soma += int(elemento)
           
        except ValueError:
            print(f"AVISO: Pulando '{elemento}' - Texto não numérico.")
           
        except TypeError:
            print(f"AVISO: Pulando '{elemento}' - Tipo de dado incompatível.")
           
    print("\n--- Resultado Final ---")
    print(f"A soma dos números que puderam ser convertidos é: {soma}")
   
    voltar_menu_principal()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_soma()

if __name__ == '__main__':
    main()