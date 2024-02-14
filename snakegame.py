import pygame
import time
import random

# speed of snake
speed_of_snake=15

# screen size
SCREEN_WIDTH=700
SCREEN_HEIGHT=460

# defining colors
midnight_blue=pygame.Color(25, 25, 112)
mint_cream=pygame.Color(245,255,250)
crimson_red=pygame.Color(220,20,60)
lawn_green=pygame.Color(124,252,0)
orange_red=pygame.Color(255,69,0)

# initializer
pygame.init()

# screen view
display_screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("my snake game")
# timer
game_clock=pygame.time.Clock()
# position of snake
position_of_snake=[100,50]
# size of the snake
body_of_snake=[
  [100,50],
  [90,50],
  [80,50],
  [70,50]
]

# position of the food
position_of_food=[
  random.randrange(1,(SCREEN_WIDTH//10)) * 10,
  random.randrange(1,(SCREEN_HEIGHT//10)) * 10
]
spawning_of_food= True

# setting  the default direction of the snake
initial_direction="RIGHT"
snake_direction=initial_direction

# setting score
player_score=0
#  function to display score
def display_score(selection, font_color, font_style, font_size):
  score_font_style=pygame.font.SysFont(font_style, font_size)
  score_surface=score_font_style.render("You Score : " + str(player_score), True, font_color)
  score_rectangle=score_surface.get_rect()
  
  # display the text
  display_screen.blit(score_surface,score_rectangle)
def game_over():
  # creat your object
  game_over_font_style=pygame.font.SysFont("time new roman", 50)
  # creating the display surface
  game_over_surface=game_over_font_style.render(
    " Your Score is :" + str(player_score), True, crimson_red
  )
  game_over_rectangle=game_over_surface.get_rect()
  
  # set position oif game over
  game_over_rectangle_midtop=(SCREEN_WIDTH/2,SCREEN_HEIGHT/4)
  
  # blit game over
  display_screen.blit(game_over_surface,game_over_rectangle)
  
  # flip() function to update smaller screen function
  pygame.display.flip()
  
  # suspending the current trade for 2seconds
  time.sleep(2)
  
  pygame.quit()
  
  quit()
# pygame.event.get()
game_run=True
# movement of the snake loop statement
while game_run:  
    # iterating through the events in the pygame.event module  
    for event in pygame.event.get():  
        # setting the variable value to False if the event's type is equivalent to pygame's QUIT constant  
        if event.type == pygame.QUIT:  
            # setting the flag value to False  
            game_run = False  
  
        # setting the variable value either to UP, DOWN, LEFT, or RIGHT  
        # if the event's type is equivalent to pygame's KEYDOWN constant,  
        # and any of the stated keys is pressed  
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_UP:  
                snake_direction = 'UP'  
            if event.key == pygame.K_DOWN:  
                snake_direction = 'DOWN'  
            if event.key == pygame.K_LEFT:  
                snake_direction = 'LEFT'  
            if event.key == pygame.K_RIGHT:  
                snake_direction = 'RIGHT'  
  
    # neglecting the action taken if the key of opposite direction is pressed  
    if snake_direction == 'UP' and initial_direction != 'DOWN':  
        initial_direction = 'UP'  
    if snake_direction == 'DOWN' and initial_direction != 'UP':  
        initial_direction = 'DOWN'   
    if snake_direction == 'LEFT' and initial_direction != 'RIGHT':  
        initial_direction = 'LEFT'   
    if snake_direction == 'RIGHT' and initial_direction != 'LEFT':  
        initial_direction = 'RIGHT'  
  
    # updating the position of the snake for every direction   
    if initial_direction == 'UP':  
        position_of_snake[1] -= 10  
    if initial_direction == 'DOWN':  
        position_of_snake[1] += 10  
    if initial_direction == 'LEFT':  
        position_of_snake[0] -= 10  
    if initial_direction == 'RIGHT':  
        position_of_snake[0] += 10  
      
    # updating the body of the snake  
    body_of_snake.insert(0, list(position_of_snake))  
    if position_of_snake[0] == position_of_food[0] and position_of_snake[1] == position_of_food[1]:  
        # incrementing the player's score by 1  
        player_score += 1  
        spawning_of_food = False  
    else:  
        body_of_snake.pop()  
  
    # randomly spawning the food  
    if not spawning_of_food:  
        position_of_food = [  
            random.randrange(1, (SCREEN_WIDTH//10)) * 10,  
            random.randrange(1, (SCREEN_HEIGHT//10)) * 10  
        ]  
    spawning_of_food = True  
  
    # filling the color on the screen  
    display_screen.fill(mint_cream)  
  
    # drawing the game objects on the screen  
    for position in body_of_snake:  
        pygame.draw.rect(display_screen, lawn_green, pygame.Rect(position[0], position[1], 10, 10))  
        pygame.draw.rect(display_screen, orange_red, pygame.Rect(position_of_food[0], position_of_food[1], 10, 10))  
  
    # conditions for the game to over  
    if position_of_snake[0] < 0 or position_of_snake[0] > SCREEN_WIDTH - 10:  
        game_over()  
    if position_of_snake[1] < 0 or position_of_snake[1] > SCREEN_HEIGHT - 10:  
        game_over()      
  
    # touching the snake body  
    for block in body_of_snake[1:]:  
        if position_of_snake[0] == block[0] and position_of_snake[1] == block[1]:  
            game_over  
  
    # displaying the score continuously  
    display_score(1, midnight_blue, 'times new roman', 20)  
  
    # refreshing the game screen  
    pygame.display.update()  
  
    # refresh rate  
    game_clock.tick(speed_of_snake)  
  
# calling the quit() function to quit the application  
pygame.quit()
      
       



