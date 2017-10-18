from os.path import join

import pygame

from .colours import BLACK, WHITE


def show_welcome_screen(screen):
    done = False

    clock = pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf', 48)
    width, height = pygame.display.get_surface().get_size()

    # TODO use package_resources
    logo = pygame.image.load(join('commandomaths',
                                  'resources',
                                  'rm-commando-logo.jpg'))

    # TODO use package_resources
    pygame.mixer.music.load(join('commandomaths',
                                  'resources',
                                  'ateam-theme.ogg'))
    pygame.mixer.music.play(start=7.8)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                # any key skips intro
                done = True

        screen.fill(WHITE)

        greeting_surface = font.render('Welcome to Commando Maths', True, BLACK)
        greeting_rect = greeting_surface.get_rect()
        greeting_rect.center = ((width / 2), (height / 6 - 40))
        screen.blit(greeting_surface, greeting_rect)

        screen.blit(logo, (width / 2 - 220, height / 2 - 260))

        pygame.display.flip()

        clock.tick(3)

    pygame.mixer.music.stop()

    return True
