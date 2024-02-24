import pygame 
 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600 

pygame.init()

# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) 
  
# Set the caption of the screen 
pygame.display.set_caption('Geeksforgeeks') 
  
# Fill the background colour to the screen 
screen.fill("black") 
  
# Update the display using flip 
pygame.display.flip() 
  
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
    pygame.draw.circle(screen, "white", cursor_position, 10, 0)
    pygame.display.flip()