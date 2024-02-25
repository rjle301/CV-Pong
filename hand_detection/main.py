import cv2
import mediapipe
import numpy as np
import pygame 
from pygame_modules.pong_shapes import *
 
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600 
PADDLE_BORDER_OFFSET = 30

capture = cv2.VideoCapture(0)
mpHands = mediapipe.solutions.hands
hands = mpHands.Hands(max_num_hands=2)
mpDraw = mediapipe.solutions.drawing_utils

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
left_paddle = Paddle(PADDLE_BORDER_OFFSET, PADDLE_BORDER_OFFSET, WINDOW_WIDTH * .02, WINDOW_HEIGHT * .15)
right_paddle = Paddle((WINDOW_WIDTH-PADDLE_BORDER_OFFSET) - WINDOW_WIDTH * .02, PADDLE_BORDER_OFFSET, WINDOW_WIDTH * .02, WINDOW_HEIGHT * .15)

# Variable to keep our game loop running 
running = True
  

# game loop 
while running: 
    success, img = capture.read()    
    
# for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

    screen.fill("black")

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
    results = hands.process(imgRGB)

    resized_image = cv2.resize(cv2.flip(img, 1), (WINDOW_WIDTH, WINDOW_HEIGHT))
    overlay = np.full(resized_image.shape, (0, 0, 0), dtype='uint8')  # Black overlay for demonstration
    cv2.addWeighted(overlay, 0.5, resized_image, 0.5, 0, resized_image)
    screen.blit(pygame.image.frombuffer(resized_image.tostring(), resized_image.shape[1::-1], "BGR"), (0, 0))


    left_fingertip_y = 0
    right_fingertip_y = 0
    
     # Draw hand landmarks on the image.
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks and connections.
            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)

            # Get the landmark that represents the tip of the index finger
            cur_landmark = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
            
            if int(cur_landmark.x * WINDOW_WIDTH) < WINDOW_WIDTH/2:
                right_fingertip_y = int(cur_landmark.y * WINDOW_HEIGHT)
            else:
                left_fingertip_y = int(cur_landmark.y * WINDOW_HEIGHT)
    
    if(left_fingertip_y != 0):
        print("Left fingertip Y:", left_fingertip_y)
        left_paddle.set_y(left_fingertip_y)
    if(right_fingertip_y != 0):
        print("Right fingertip Y:", right_fingertip_y)
        right_paddle.set_y(right_fingertip_y)

    left_paddle.draw(screen, "white") 
    right_paddle.draw(screen, "white")
        
    pygame.display.flip()
