import operator
from os.path import join

from pkg_resources import resource_filename
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
    QUESTION_Y_POSITION = 600
    OPTIONS_X_POSITION = 820
    OPTIONS_TOP_POSITION = 380
    SOLDIER_X_OFFSET = 70
    SOLDIER_Y_OFFSET = 120
    TEXT_Y_OFFSET = 100

    NUM_SOLDIERS_PER_ROW = 3

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('freesansbold.ttf', 115)
        self.soldier_image = \
            pygame.image.load(resource_filename(__name__,
                                                join('resources',
                                                     'soldier.png')))

    def render_question(self, question):
        self.screen.fill(WHITE)

        # render the text question
        self._render_number(question['lhs'],
                            (100, type(self).QUESTION_Y_POSITION))
        text_y_position = \
            type(self).QUESTION_Y_POSITION - type(self).TEXT_Y_OFFSET
        self._render_text(question['operation'],
                          (300, text_y_position))
        self._render_number(question['rhs'],
                            (500, type(self).QUESTION_Y_POSITION))
        self._render_text('=', (680, text_y_position))
        self._render_answers(question['options'],
                             (type(self).OPTIONS_X_POSITION,
                              type(self).OPTIONS_TOP_POSITION))
        pygame.display.flip()

    def _render_number(self, number, position):
        self._render_text(str(number), position)
        position = position[0] - 60, position[1] - 180
        x, y = position
        for i in range(number):
            x += type(self).SOLDIER_X_OFFSET
            if i % type(self).NUM_SOLDIERS_PER_ROW == 0:
                x = position[0]
                y -= type(self).SOLDIER_Y_OFFSET
            self._render_soldier((x, y))

    def _render_text(self, text, position):
        surface = self.font.render(text, True, BLACK)
        rect = surface.get_rect()
        rect.center = position
        self.screen.blit(surface, rect)
        # rect.center = position[0], position[1] - 180
        # self.screen.blit(surface, rect)

    def _render_soldier(self, position):
        self.screen.blit(self.soldier_image, position)

    def _render_answer_button(self, answer, position):
        # TODO render button
        surface = self.font.render(str(answer), True, BLACK)
        rect = surface.get_rect()
        rect.center = position
        self.screen.blit(surface, rect)

    def _render_answers(self, answers, position):
        x, y = position
        for i, answer in enumerate(answers):
            y = position[1] + i * 150
            self._render_answer_button(answer, (x, y))


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
