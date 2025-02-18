# Import modules
import pygame
import time
# Initialise pygame module
pygame.init()

# Makes screen
screen = pygame.display.set_mode((900, 600))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - By Robson Butler")

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (246, 38, 38)
green = (62, 218, 67)

# Fonts
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)

clock = pygame.time.Clock()


quit_game = False

snake_x = 440
snake_y = 290

snake_x_change = 0
snake_y_change = 0

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

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green)

    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(15)

pygame.quit()
quit()
