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


def player_score(score, score_colour):
    display_score = score_font.render(f"Score: {score}", True,
                                      score_colour)
    screen.blit(display_score, (780, 20))


def draw_snake(snake_list):
    print(f"Snake List: {snake_list}")
    for i in snake_list:
        pygame.draw.rect(screen, red, [i[0], i[1], 20, 20])


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
    snake_list = []
    snake_length = 1

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

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
             if x == snake_head:
                 game_over = True

        draw_snake(snake_list)

        score = snake_length - 1
        player_score(score, black)


        food = pygame.Rect(food_x, food_y, 20, 20)
        # Use 'convert_alpha' for png files but use 'convert' for jpg
        apple = pygame.image.load('apple_3.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        screen.blit(resized_apple, food)

        pygame.display.update()

        print(f"Snake X: {snake_x}")
        print(f"Food X: {food_x}")
        print(f"Snake Y: {snake_y}")
        print(f"Food Y: {food_y}")

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(20, 900 - 20) / 20) * 20
            food_y = round(random.randrange(20, 660 - 20) / 20) * 20
            # Testing
            print("Got it")
            
            snake_length += 1


        clock.tick(5)


    pygame.quit()
    quit()


# Main routine
game_loop()
