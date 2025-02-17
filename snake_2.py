import pygame
import time
pygame.init()

screen = pygame.display.set_mode((900, 600))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - By Robson Butler")


time.sleep(5)

pygame.quit()
quit()
