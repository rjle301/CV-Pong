import pygame

class Ball:
    def __init__(self, x_pos, y_pos, radius):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.velocity_y = 5
        self.velocity_x = 7

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.x_pos, self.y_pos), self.radius, 0)
    
    def move(self):
        self.x_pos += self.velocity_x
        self.y_pos += self.velocity_y

    def flip_x_velocity(self):
        self.velocity_x *= -1
    
    def flip_y_velocity(self):
        self.velocity_y *= -1