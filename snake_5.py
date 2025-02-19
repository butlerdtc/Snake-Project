# Import modules
import pygame
import time
import random
# Initialise pygame module
pygame.init()

# Makes screen
screen = pygame.display.set_mode((1000, 720))
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


def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)


clock = pygame.time.Clock()


quit_game = False

snake_x = 490
snake_y = 350

snake_x_change = 0
snake_y_change = 0

food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
food_y = round(random.randrange(20, 720 - 20) / 20) * 20

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

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

    if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y < 0:
        quit_game = True

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green)

    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    pygame.draw.circle(screen, yellow, [food_x, food_y], 10)
    pygame.display.update()

    if snake_x == food_x - 10 and snake_y == food_y - 10:
        food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
        food_y = round(random.randrange(20, 720 - 20) / 20) * 20
        
    clock.tick(5)

message("You died!", black, white)
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()
