import random 

def determinar_vencedor(jogador, PC):
    if jogador == PC:
        return 'Empate'
    elif (jogador == 'pedra' and PC == 'tesoura') or \
         (jogador == 'tesoura' and PC == 'papel') or \
         (jogador == 'papel' and PC == 'pedra'):
        return 'Tu venceu'
    else:
        return 'A vitoria e do PC'
opcoes = ['pedra', 'tesoura', 'papel']
vitorias_jogador = 0
vitorias_computador = 0

while True:
    jogador = input("Escolha: pedra, tesoura ou papel (ou 'sair' para encerrar): ").lower()
    if jogador == 'sair':
        print(f'Jogo encerrado. Placar final - Tu: {vitorias_jogador} | PC: {vitorias_computador}')
        break
    if jogador not in opcoes:
        print('Opção inválida. Tente novamente.')
        continue
    
    PC = random.choice(opcoes)
    print(f"Escolha do PC: {PC}")
    
    resultado = determinar_vencedor(jogador, PC)
    print(resultado)

    if 'Tu venceu' in resultado:
        vitorias_jogador += 1
    elif 'A vitoria e do PC' in resultado:
        vitorias_computador += 1
    
    print(f'Placar atual - Tu: {vitorias_jogador} | PC: {vitorias_computador}\n')