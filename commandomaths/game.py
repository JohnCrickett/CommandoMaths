import operator

import pygame

from .colours import WHITE


def _next_question():
    return \
        {
            'lhs': 1,
            'rhs': 2,
            'operation': operator.add,
            'options': [1, 3, 7]
        }


def _render_question_on_screen(question, screen):
    pass


def run_game_loop(screen):
    done = False

    clock = pygame.time.Clock()

    question = _next_question()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # any key skips intro
                done = True

        screen.fill(WHITE)

        # --- Drawing code should go here
        _render_question_on_screen(question, screen)

        pygame.display.flip()

        # --- Limit to 20 frames per second
        clock.tick(20)
