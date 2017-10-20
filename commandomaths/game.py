import operator
from os.path import join

import pygame

from .colours import BLACK, WHITE

OPERATORS = \
    {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }


def _next_question():
    # TODO question generator
    return \
        {
            'lhs': 1,
            'rhs': 2,
            'operation': '+',
            'options': [1, 3, 7]
        }


class GameScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('freesansbold.ttf', 115)
        # TODO use package resources
        self.soldier_image = \
            pygame.image.load(join('commandomaths',
                                   'resources',
                                   'soldier.png'))

    def render_question(self, question):
        self.screen.fill(WHITE)

        # render the text question
        self._render_number(question['lhs'], (100, 300))
        self._render_text(question['operation'], (300, 300))
        self._render_number(question['rhs'], (500, 300))
        self._render_text('=', (600, 300))
        self._render_answers(question['options'], (800, 200))
        pygame.display.flip()

    def _render_number(self, number, position):
        self._render_text(str(number), position)
        x, y = position
        for i in range(number):
            x += 70
            if i % 3:
                x = position[0]
                y += 120
            self._render_soldier((x, y))

    def _render_text(self, text, position):
        surface = self.font.render(text, True, BLACK)
        rect = surface.get_rect()
        rect.center = position
        self.screen.blit(surface, rect)

    def _render_soldier(self, position):
        self.screen.blit(self.soldier_image, position)

    def _render_answers(self, options, position):
        pass


def run_game_loop(screen):
    done = False

    clock = pygame.time.Clock()

    game_screen = GameScreen(screen)

    question = _next_question()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        game_screen.render_question(question)

        clock.tick(20)
