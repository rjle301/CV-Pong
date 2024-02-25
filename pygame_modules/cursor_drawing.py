import cv2
import mediapipe
import pygame 
from pong_shapes import *
 
# Window constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600 

# Paddle constants
PADDLE_WIDTH = WINDOW_WIDTH * .02
PADDLE_HEIGHT = WINDOW_HEIGHT * .15
PADDLE_BORDER_OFFSET = 30

# Ball constants
START_X = WINDOW_WIDTH / 2
START_Y = WINDOW_HEIGHT / 2
RADIUS = 7

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
left_paddle = Paddle(PADDLE_BORDER_OFFSET, PADDLE_BORDER_OFFSET, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = Paddle(WINDOW_WIDTH - (PADDLE_WIDTH + PADDLE_BORDER_OFFSET), PADDLE_BORDER_OFFSET, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_list = [left_paddle, right_paddle]
ball = Ball(START_X, START_Y, RADIUS)
  
# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    
    # for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

    cursor_x, cursor_y = pygame.mouse.get_pos()
    
    # If the cursor goes out of the game window, or the cursor gets too close to
    # the bottom of the game window, the paddle is snapped to the bottom of the game window
    if (not pygame.mouse.get_focused()) or (cursor_y > WINDOW_HEIGHT - PADDLE_HEIGHT):
        if cursor_y > WINDOW_HEIGHT / 2:
            left_paddle.set_y(WINDOW_HEIGHT - PADDLE_HEIGHT)
            right_paddle.set_y(WINDOW_HEIGHT - PADDLE_HEIGHT)
        else:
            left_paddle.set_y(0)
            right_paddle.set_y(0)
    else:
        left_paddle.set_y(cursor_y)
        right_paddle.set_y(cursor_y)
        
    ball.move()
    
    for paddle in paddle_list:
        if (paddle.get_rectangle().colliderect(pygame.Rect(ball.get_x() - ball.get_radius(), ball.get_y() - ball.get_radius(), ball.get_diameter(), ball.get_diameter()))):
            ball.flip_x_velocity()
        
    if (ball.get_y() - ball.get_radius()) <= 0 or (ball.get_y() + ball.get_radius() >= WINDOW_HEIGHT):
        ball.flip_y_velocity()
        
    screen.fill("black")
    left_paddle.draw(screen, "white")
    right_paddle.draw(screen, "white")
    ball.draw(screen, "white")
    pygame.display.flip()

