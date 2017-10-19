import pygame


def init_screen():
    # TODO get screen size and size window based on it
    # display_info = pygame.display.Info()
    # print(display_info)
    size = 1280, 800

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Commando Maths")

    return screen
