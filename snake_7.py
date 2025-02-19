# Import modules
import pygame
import time
import random
# Initialise pygame module
pygame.init()

# Makes screen
screen = pygame.display.set_mode((900, 660))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - By Robson Butler")

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (246, 38, 38)
green = (62, 218, 67)
yellow = (255, 255, 0)

# Fonts
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

clock = pygame.time.Clock()

def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    text_box = txt.get_rect(center=(450, 330))
    screen.blit(txt, text_box)


def game_loop():
    quit_game = False
    game_over = False

    snake_x = 440
    snake_y = 320

    snake_x_change = 0
    snake_y_change = 0

    food_x = round(random.randrange(20, 900 - 20) / 20) * 20
    food_y = round(random.randrange(20, 660 - 20) / 20) * 20

    while not quit_game:
        while game_over:
            screen.fill(white)
            message("You died! Press 'Q' to Quit or 'A' to Play Again",
                    black, white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = ("Exit: 'X' to Quit, 'SPACE' to Resume, 'R' to"
                                " Reset")
                message(instructions, white, black)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                end = True, game_loop()
                            if event.key == pygame.K_SPACE:
                                end = True
                            if event.key == pygame.K_q:
                                quit_game = True
                                end = True
                            if event.key == pygame.K_x:
                                quit_game = True
                                end = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -20
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = 20
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_x_change = 0
                    snake_y_change = -20
                elif event.key == pygame.K_DOWN:
                    snake_x_change = 0
                    snake_y_change = 20

        if snake_x >= 900 or snake_x < 0 or snake_y >= 660 or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)

        pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
        pygame.display.update()

        pygame.draw.circle(screen, yellow, [food_x + 10, food_y + 10],
                           10)
        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(20, 900 - 20) / 20) * 20
            food_y = round(random.randrange(20, 660 - 20) / 20) * 20

        clock.tick(5)


    pygame.quit()
    quit()


# Main routine
game_loop()
