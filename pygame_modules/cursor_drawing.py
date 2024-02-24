import cv2
import mediapipe
import pygame 
from paddle import *
 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600 

PADDLE_WIDTH = WINDOW_WIDTH * .02
PADDLE_HEIGHT = WINDOW_HEIGHT * .15

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
left_paddle = Paddle(30, 30, PADDLE_WIDTH, WINDOW_HEIGHT * .15)
right_paddle = Paddle(770 - WINDOW_WIDTH * .02, 30, PADDLE_WIDTH, PADDLE_HEIGHT)
  
# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    #success, img = capture.read()
    #hand_location = get_hand_location(img)
    
    
# for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False


    screen.fill("black")

    cursor_x, cursor_y = pygame.mouse.get_pos()
    # print([cursor_x, cursor_y])
    print(pygame.mouse.get_focused())
    if not pygame.mouse.get_focused():
        if cursor_y > WINDOW_HEIGHT / 2:
            left_paddle.setY(WINDOW_HEIGHT - PADDLE_HEIGHT)
            right_paddle.setY(WINDOW_HEIGHT - PADDLE_HEIGHT)
        else:
            left_paddle.setY(0)
            right_paddle.setY(0)
    else:
        left_paddle.setY(cursor_y)
        right_paddle.setY(cursor_y)
        
    left_paddle.draw(screen, "white")
    right_paddle.draw(screen, "white")
    pygame.display.flip()