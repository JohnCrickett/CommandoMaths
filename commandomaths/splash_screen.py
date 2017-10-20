from os.path import join

import pygame

from .colours import BLACK, WHITE


class SplashScreen:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.font = pygame.font.Font('freesansbold.ttf', 48)
        self.width = width
        self.height = height
        # TODO use package_resources
        self.logo = pygame.image.load(join('commandomaths',
                                           'resources',
                                           'rm-commando-logo.jpg'))

    def render(self):
        self.screen.fill(WHITE)

        greeting_surface = \
            self.font.render('Welcome to Commando Maths', True, BLACK)
        greeting_rect = greeting_surface.get_rect()
        greeting_rect.center = ((self.width / 2), (self.height / 6 - 40))
        self.screen.blit(greeting_surface, greeting_rect)

        self.screen.blit(self.logo,
                         (self.width / 2 - 220, self.height / 2 - 260))

        pygame.display.flip()


def show_splash_screen(screen):
    done = False

    clock = pygame.time.Clock()

    width, height = pygame.display.get_surface().get_size()
    splash_screen = SplashScreen(screen, width, height)

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

        splash_screen.render()

        clock.tick(3)

    pygame.mixer.music.stop()

    return True
