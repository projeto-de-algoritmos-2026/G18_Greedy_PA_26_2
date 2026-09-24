#--- import sistema
import curses
from minigame import testbench
from minigame import rodada

#--- variaveis do jogo
game_var = {
    'moedas' : [500,100,50,10,5,1],
    'pontuacao_por_rodada' : 100,
    'tempo_limite' : 20
}

def menu_principal(stdscr):
    curses.curs_set(0)

    while True:
        stdscr.erase()
        stdscr.border()

        stdscr.addstr(2, 4, "=== TROCO AMBICIOSO ===", curses.A_BOLD)
        stdscr.addstr(4, 4, "1 - Iniciar Expediente (Jogar)")
        stdscr.addstr(5, 4, "2 - Fechar a Loja (Sair)")
        stdscr.addstr(7, 4, "Escolha uma opcao: ")
        stdscr.refresh()

        opcao = stdscr.getch()

        if opcao == 49:
            testbench(stdscr)
        elif opcao == 50:
            break


if __name__ == "__main__":
    curses.wrapper(menu_principal)
