import os

distancia = []
velocidade = []
tempo = []

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)

def voltar_em_coleta():    
    input('\nPressione um botão para voltar à coleta de dados...')
    main()

def coletar_dados():
    exibir_subtitulo('Coleta de Dados da Viagem\n')
   
    try:
        dist = float(input('Digite a distância entre os lugares (km): '))
        vel = float(input('Digite a velocidade média da sua viagem (km)/h: '))
       
        distancia.append(dist)
        velocidade.append(vel)

        return True
   
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

        return False

def calcular_tempo_viagem(dist, vel):

    global tempo

    try:
        tempo_calculado = dist / vel
        tempo.append(tempo_calculado)

    except ZeroDivisionError:
        tempo.append('Erro, valores nao podems ser igual à 0')
   
def exibir_resultados():

    exibir_subtitulo('Resultados da Viagem\n')
    if not distancia:
        print("Nenhum dado válido para exibir.")
        voltar_em_coleta()
        return

    for i in range(len(distancia)):
        resultado_tempo = tempo[i]
       
        if isinstance(resultado_tempo, str):
            print(f'Para {distancia[i]:.2f}km a {velocidade[i]:.2f}km/h: {resultado_tempo}')
        else:
            print(f'Para {int(distancia[i])}km a {int(velocidade[i])}km/h, o tempo é: {int(velocidade[i])} horas')
   
    # Pausa o programa para o usuário ver os resultados
    voltar_em_coleta()

def main():
   
    coleta_bem_sucedida = coletar_dados()
   
    if coleta_bem_sucedida:
        ultima_distancia = distancia[-1]
        ultima_velocidade = velocidade[-1]
       
        calcular_tempo_viagem(ultima_distancia, ultima_velocidade)
       
    exibir_resultados()

if __name__ == '__main__':
    main()