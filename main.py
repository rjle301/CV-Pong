import cv2
import mediapipe
import pygame 
import random
import numpy as np
import pygame_modules.pong_shapes as pong_shapes
import pygame_modules.player as player
 

def get_dotted_line_segments(window_width, window_height):
    segments = []
    center_of_screen = window_width/2
    num_lines = window_height // 20
    for _, v in enumerate(range(0, window_height, num_lines)):
        segments.append(pygame.Rect(center_of_screen - HORIZONTAL_LINE_OFFSET, v + HORIZONTAL_LINE_OFFSET, LINE_WIDTH, LINE_HEIGHT))
        
    return segments


# Window constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600 

# Text constants
PLAYER_1_SCORE_POS_OFFSET = WINDOW_WIDTH/4
PLAYER_2_SCORE_POS_OFFSET = 3 * WINDOW_WIDTH / 4

# Paddle constants
PADDLE_WIDTH = WINDOW_WIDTH * .02
PADDLE_HEIGHT = WINDOW_HEIGHT * .15
PADDLE_BORDER_OFFSET = 30

# Ball constants
START_X = WINDOW_WIDTH / 2
START_Y = WINDOW_HEIGHT / 2
RADIUS = 7

# Dashed line constants
VERTICAL_LINE_OFFSET = 7.5
HORIZONTAL_LINE_OFFSET = 3
LINE_WIDTH = 6
LINE_HEIGHT = 15

capture = cv2.VideoCapture(0)
mpHands = mediapipe.solutions.hands
hands = mpHands.Hands(max_num_hands=2)
mpDraw = mediapipe.solutions.drawing_utils

pygame.init()
pygame.font.init()

# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) 
my_font = pygame.font.SysFont('Monospaced', 150, 'white')
  
# Set the caption of the screen 
pygame.display.set_caption('CV Pong') 
  
# Fill the background colour to the screen 
screen.fill("black") 
  
# Update the display using flip 
pygame.display.flip() 

#Initialize two paddles - left and right
left_paddle = pong_shapes.Paddle(PADDLE_BORDER_OFFSET, PADDLE_BORDER_OFFSET, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pong_shapes.Paddle(WINDOW_WIDTH - (PADDLE_WIDTH + PADDLE_BORDER_OFFSET), PADDLE_BORDER_OFFSET, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_list = [left_paddle, right_paddle]
ball = pong_shapes.Ball(START_X, START_Y, RADIUS)
  
# Variable to keep our game loop running 
running = True

segments = get_dotted_line_segments(WINDOW_WIDTH, WINDOW_HEIGHT)
player1, player2 = player.Player(), player.Player()

# game loop 
while running: 
    success, img = capture.read()  
    # for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
    
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
        left_paddle.set_y(left_fingertip_y)
    if(right_fingertip_y != 0):
        right_paddle.set_y(right_fingertip_y)
        
    ball.move()
    
    # Check to see if a ball collided with a paddle
    for paddle in paddle_list:
        if (paddle.get_rectangle().colliderect(pygame.Rect(ball.get_x() - ball.get_radius(), ball.get_y() - ball.get_radius(), ball.get_diameter(), ball.get_diameter()))):
            ball.flip_x_velocity()
    
    # Check to see if the ball went out of bounds
    if (ball.get_x() + ball.get_radius() < 0 or ball.get_x() - ball.get_radius() > WINDOW_WIDTH):
        if ball.get_x() + ball.get_radius() < 0:
            player2.increment_score()
        else:
            player1.increment_score()
            
        ball.reset(WINDOW_WIDTH, random.randint(100, 500))
        
            
    
    # Check if the ball hit the bottom or top of the game window
    if (ball.get_y() - ball.get_radius()) <= 0 or (ball.get_y() + ball.get_radius() >= WINDOW_HEIGHT):
        ball.flip_y_velocity()
        
    for rect in segments:
        pygame.draw.rect(screen, "white", rect)

    left_paddle.draw(screen, "white")
    right_paddle.draw(screen, "white")
    ball.draw(screen, "white")

    player1_text = my_font.render(player1.get_score_str(), False, (255, 255, 255))
    player2_text = my_font.render(player2.get_score_str(), False, (255, 255, 255))
    
    player1_text_width, player1_text_height = player1_text.get_size()
    player2_text_width, player2_text_height = player2_text.get_size()

    screen.blit(player1_text, (PLAYER_1_SCORE_POS_OFFSET - player1_text_width/2, 0))
    screen.blit(player2_text, (PLAYER_2_SCORE_POS_OFFSET - player2_text_width/2, 0))

    pygame.display.flip()