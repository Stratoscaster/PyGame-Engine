from tools.setup import *
import tools.constants as c

def main():
    initialize()
    display = get_display()
    # load_gfx()
    clock = get_clock()
    game_states = get_game_states()
    controller = get_controller(display, clock, game_states, c.STARTING_STATE)

    controller.run_game()


if __name__ == '__main__':
    main()



















