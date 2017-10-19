import os
from pkg_resources import get_distribution

import pygame

from .game import run_game_loop
from .screen import init_screen
from .splash_screen import show_splash_screen


def main():
    print('Welcome to Commando Maths Version {}'
          .format(get_distribution("commandomaths").version))

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    screen = init_screen()

    if show_splash_screen(screen):
        run_game_loop(screen)

    pygame.quit()


if __name__ == '__main__':
    main()
