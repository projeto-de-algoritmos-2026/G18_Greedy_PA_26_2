#--- import sistema
import curses
from minigame import testbench
from minigame import rodada



def menu_principal(stdscr):
    game_var = {
        'moedas': [500, 100, 50, 10, 5, 1],
        'pontuacao_por_rodada': 100,
        'tempo_limite': 20
    }
    player_pontuacao = 100

    while True:
        stdscr.erase()
        curses.curs_set(0)
        stdscr.border()

        stdscr.addstr(2, 4, "=== TROCO AMBICIOSO ===", curses.A_BOLD)
        stdscr.addstr(4, 4, f"Pontuação Atual: {player_pontuacao}")
        stdscr.addstr(5, 4, "[ 1 ] - Atender próximo cliente")
        stdscr.addstr(6, 4, "[ 2 ] - Fechar a Loja (Sair)")
        stdscr.addstr(8, 4, "Escolha uma opcao: ")
        stdscr.refresh()

        stdscr.nodelay(False)
        opcao = stdscr.getch()

        if opcao == ord('1'):
            pontos_ganhos = rodada(stdscr,game_var)
            player_pontuacao += pontos_ganhos

            if player_pontuacao <= 0:
                stdscr.erase()
                stdscr.addstr(2, 4, "GAME OVER", curses.A_BOLD)
                stdscr.addstr(4, 4, f"Sua pontuação chegou a zero (ou até menos que isso!). ({player_pontuacao})")
                stdscr.addstr(5, 4, "A loja faliu e você foi demitido... Que pena.")
                stdscr.addstr(7, 4, "Pressione qualquer tecla para sair do jogo...")
                stdscr.refresh()
                stdscr.getch()
                break
        elif opcao == ord('2'):
            break


if __name__ == "__main__":
    curses.wrapper(menu_principal)
