"""Snake Game final version - Created by Robson Butler 25/02/25 """

# Import modules
import pygame
import random
# Initialise pygame module
pygame.init()

# Makes screen and sets icon and name for the display
screen = pygame.display.set_mode((900, 660))
# Loads the image file to use for the windows icon
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - By Robson Butler")

# Global colour variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (246, 38, 38)
green = (62, 218, 67)
yellow = (255, 255, 0)

# Fonts for the scores and other messages

# SysFont means it uses the name and searches the system for that font while
# Font requires the file path and availability can vary between systems
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

# Sets the speed at which the snake moves
clock = pygame.time.Clock()


# Function to keep track of high score in a text file
def load_high_score():
    # This checks if the HI_score.txt file exists and opens it as read only
    try:
        hi_score_file = open("HI_score.txt", 'r')
    # If file does not exist it creates it and writes default value of 0
    except IOError:
        hi_score_file = open("HI_score.txt", 'w')
        hi_score_file.write("0")
    # Then it reads the file and sets value as number in file then closes file
    hi_score_file = open("HI_score.txt", 'r')
    value = hi_score_file.read()
    hi_score_file.close()
    # Returns the current high score
    return value


# Function to update text file with new high score
def update_high_score(score, high_score):
    # Checks if new score is greater than current high score
    if int(score) > int(high_score):
    # Returns the highest of the two scores
        return score
    else:
        return high_score


# Saves the updated high score to text file if greater than old high score
def save_high_score(high_score):
    # Opens HI_score.txt file then writes the new score then closes the file
    high_score_file = open("HI_score.txt", 'w')
    high_score_file.write(str(high_score))
    high_score_file.close()

# Displays the current score and high score for the game
def player_score(score, score_colour, hi_score):
    # Renders creates an 'object' for the text to display, antialiasing
    # smoothes the edges, next two arguments are for font/bkgd colour
    display_score = score_font.render(f"Score: {score}", True,
                                      score_colour)
    # Blit draws the text/image (score) onto another image (screen)
    screen.blit(display_score, (780, 20))

    display_score = score_font.render(f"High Score: {hi_score}",
                                      True, score_colour)
    screen.blit(display_score, (10, 10))


# Function to draw the snake
def draw_snake(snake_list):
    # print(f"Snake List: {snake_list}") - Testing to print coordinates of
    # snake body

    # This iterates through each pair of coordinates in the list
    for i in snake_list:
        # This draws a rectangle on the screen, colours it red then the next
        # brackets hold the location of the rectangle and then dimensions
        pygame.draw.rect(screen, red, [i[0], i[1], 20, 20])


# Function to display a message in the center of the screen
def message(msg, txt_colour, bkgd_colour):
    # Creates the text to display - Check line 71
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Center sets the center of the rectangle to be the coordinates given
    text_box = txt.get_rect(center=(450, 330))

    # Draws the text onto the textbox - Check line 75
    screen.blit(txt, text_box)

# Function to run the game
def game_loop():
    # Sets the game control variables to False
    quit_game = False
    game_over = False

    # Sets initial coordinates of snake to center of screen
    # ((length/width of screen - 20) / 2)
    snake_x = 440
    snake_y = 320

    # Initialises the change in x and y value of snake to 0
    snake_x_change = 0
    snake_y_change = 0
    # Makes the list of snake coordinates and sets default snake length to 1
    snake_list = []
    snake_length = 1

    # Randomly sets coordinates of the food

    # Random range starts at 20 and ends at 880 as food is 20 px wide so this
    # makes it so it will never be off-screen, dividing, rounding and
    # multiplying by 20 ensures it will always be in increments of 20
    food_x = round(random.randrange(20, 900 - 20) / 20) * 20
    food_y = round(random.randrange(20, 660 - 20) / 20) * 20

    high_score = load_high_score()
    
    while not quit_game:
        while game_over:
            save_high_score(high_score)
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
        player_score(score, black, high_score)

        high_score = update_high_score(score, high_score)

        if score > 3:
            speed = score
        else:
            speed = 3


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


        clock.tick(speed)


    pygame.quit()
    quit()


# Main routine
game_loop()
