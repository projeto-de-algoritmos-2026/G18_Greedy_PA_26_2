import curses
import time
import random

from algoritmo import calc_troco_guloso

def rodada(stdscr,game_settings:dict) -> int:
    stdscr.nodelay(True)
    curses.curs_set(1)

    moedas = sorted(game_settings['moedas'],reverse=True)
    pontuacao_por_rodada = int(game_settings['pontuacao_por_rodada'])
    tempo_limite = int(game_settings['tempo_limite'])

    rodada_preco = random.randint(15,10600)

    rodada_pagamentos_possiveis = [
        ((rodada_preco // 10) + 1) * 10,
        ((rodada_preco // 50) + 1) * 50,
        ((rodada_preco // 100) + 1) * 100,
        ((rodada_preco // 500) + 1) * 500,
        ((rodada_preco // 1000) + 1) * 1000,
        5000,
        10000
    ]
    rodada_pagamentos_validos = list(set([p for p in rodada_pagamentos_possiveis if p > rodada_preco]))

    rodada_pagamento = random.choice(rodada_pagamentos_validos)
    rodada_troco = rodada_pagamento-rodada_preco

    resposta_ideal = calc_troco_guloso(moedas,rodada_troco)
    resposta_player = [0]*len(moedas)
    moeda_idx = 0

    tempo_comeco = time.time()
    user_input = ""

    #--- rodada -> comecou

    while True:
        decorrido = time.time() - tempo_comeco
        tempo_restante = int(tempo_limite - decorrido)

        if tempo_restante <= 0:
            break

        stdscr.erase()
        stdscr.border()

        stdscr.addstr(1,4,f"TEMPO RESTANTE: {tempo_restante}s", curses.A_BOLD)
        stdscr.addstr(3, 4, f"Compra: ¥ {rodada_preco} | Pagamento: ¥ {rodada_pagamento}")
        stdscr.addstr(4, 4, f"TROCO ALVO: ¥ {rodada_troco}", curses.A_REVERSE)

        game_rodada_moeda_linha = 5
        for i, moeda in enumerate(moedas):
            game_rodada_moeda_linha += 1
            if i < moeda_idx:
                stdscr.addstr(game_rodada_moeda_linha, 5, f"Moeda de ¥ {moeda}: {resposta_player[i]}")
            elif i == moeda_idx:
                stdscr.addstr(game_rodada_moeda_linha, 5, f"Moeda de ¥ {moeda}: {user_input}_")
            else:
                stdscr.addstr(game_rodada_moeda_linha, 5, f"Moeda de ¥ {moeda}: ")

        stdscr.addstr(game_rodada_moeda_linha + 2, 4, "(Digite a quantidade e pressione ENTER)")
        stdscr.refresh()

        try:
            char = stdscr.getch()
            if char != -1:
                if char in (10, 13):  # Enter
                    qtd = int(user_input) if user_input.isdigit() else 0
                    resposta_player[moeda_idx] = qtd
                    moeda_idx += 1
                    user_input = ""
                    if moeda_idx >= len(moedas):
                        break
                elif char in (8, 127, curses.KEY_BACKSPACE):
                    user_input = user_input[:-1]
                else:
                    user_input += chr(char)
        except Exception:
            pass

        time.sleep(0.05)

    #--- rodada -> pontuacao final

    stdscr.erase()
    stdscr.border()

    curses.curs_set(0)
    rodada_pontuacao = 0

    if tempo_restante <= 0:
        rodada_pontuacao = -int(pontuacao_por_rodada)
        stdscr.addstr(1, 4, "O tempo acabou! E o cliente foi embora... :(", curses.A_BOLD)
        stdscr.addstr(2, 4, f"{rodada_pontuacao} pontos!", curses.A_REVERSE)
    else:
        total_entregue = sum(int(moedas[i]) * resposta_player[i] for i in range(len(moedas)))
        moedas_usadas_jogador = sum(resposta_player)
        moedas_usadas_ideal = sum(resposta_ideal.values())

        stdscr.addstr(1, 4, f"Troco Necessário: ¥ {rodada_troco} | Você Entregou: ¥ {total_entregue}")

        if total_entregue != rodada_troco:
            rodada_pontuacao = -int(pontuacao_por_rodada * (tempo_restante/tempo_limite))
            stdscr.addstr(2, 4, "O que você tá fazendo?! Você devolveu o troco errado...)")
            stdscr.addstr(3, 4, f"{rodada_pontuacao} pontos!", curses.A_REVERSE)
        elif moedas_usadas_jogador == moedas_usadas_ideal:
            rodada_pontuacao = int(pontuacao_por_rodada * (tempo_restante/tempo_limite))
            stdscr.addstr(2, 4, f"PERFEITO! Você entregou o troco exato utilizando {moedas_usadas_jogador} moedas.", curses.A_BOLD)
            stdscr.addstr(3, 4, f"+{rodada_pontuacao} pontos!", curses.A_REVERSE)
        else:
            rodada_pontuacao = int(pontuacao_por_rodada * (5 / tempo_limite))
            stdscr.addstr(2, 4, f"Ok! Você entregou o troco exato utilizando {moedas_usadas_jogador} moedas.")
            stdscr.addstr(3, 4, f"Porém ideal era utilizar apenas {moedas_usadas_ideal} moedas.")
            stdscr.addstr(4, 4, f"+{rodada_pontuacao} pontos!", curses.A_REVERSE)

    stdscr.addstr(6, 4, "Pressione qualquer tecla para continuar...")
    stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.getch()

    return rodada_pontuacao

def testbench(stdscr):
    bench_game_settings = {
        'moedas': [500, 100, 50, 10, 5, 1],
        'pontuacao_por_rodada': 100,
        'tempo_limite': 20
    }
    bench_pontuacao = 100

    while True:
        bench_rodada = rodada(stdscr,bench_game_settings)
        bench_pontuacao += bench_rodada

        if bench_pontuacao <= 0:
            stdscr.erase()
            stdscr.addstr(2, 4, "GAME OVER | Não sobra nada pro beta", curses.A_BOLD)
            stdscr.addstr(4, 4, f"Sua pontuação chegou a zero (ou até menos que isso!). ({bench_pontuacao})")
            stdscr.addstr(5, 4, "A loja faliu e você foi demitido.")
            stdscr.addstr(7, 4, "Pressione qualquer tecla para sair do jogo...")
            stdscr.refresh()
            stdscr.getch()
            break

if __name__ == '__main__':
    curses.wrapper(testbench)


