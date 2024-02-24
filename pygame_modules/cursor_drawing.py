import pygame 
from paddle import *
 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600 

pygame.init()

# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) 
  
# Set the caption of the screen 
pygame.display.set_caption('Cursor tracking') 
  
# Fill the background colour to the screen 
screen.fill("black") 
  
# Update the display using flip 
pygame.display.flip() 

#Initialize two paddles - left and right
left_paddle = Paddle(30, 30, WINDOW_WIDTH * .02, WINDOW_HEIGHT * .15)
right_paddle = Paddle(770 - WINDOW_WIDTH * .02, 30, WINDOW_WIDTH * .02, WINDOW_HEIGHT * .15)
  
# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False


    screen.fill("black")

    cursor_position = pygame.mouse.get_pos()
    left_paddle.draw(screen, "white")
    right_paddle.draw(screen, "white")
    pygame.display.flip()