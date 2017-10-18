import pygame


def init_screen():
    size = width, height = 1280, 800

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Commando Maths")

    return screen
