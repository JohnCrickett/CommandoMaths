import operator

import pygame

from .colours import BLACK, WHITE


def _next_question():
    return \
        {
            'lhs': 1,
            'rhs': 2,
            'operation': operator.add,
            'options': [1, 3, 7]
        }


def _render_question_on_screen(question, font, screen):
    # render the text question
    lhs_surface = font.render(str(question['lhs']), True, BLACK)
    lhs_rect = lhs_surface.get_rect()
    lhs_rect.center = 100, 300
    screen.blit(lhs_surface, lhs_rect)

    # render a group of soldiers the size of each part of the question
    # above the text

    # display the new screen
    pygame.display.flip()


def run_game_loop(screen):
    done = False

    clock = pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf', 115)

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
        _render_question_on_screen(question, font, screen)

        pygame.display.flip()

        # --- Limit to 20 frames per second
        clock.tick(20)
