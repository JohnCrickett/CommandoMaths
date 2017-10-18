from pkg_resources import get_distribution

import pygame

from .game import run_game_loop
from .screen import init_screen
from .welcome_screen import show_welcome_screen


def main():
    print('Welcome to Commando Maths Version {}'
          .format(get_distribution("commandomaths").version))

    pygame.init()

    screen = init_screen()

    if show_welcome_screen(screen):
        run_game_loop(screen)

    pygame.quit()


if __name__ == '__main__':
    main()
