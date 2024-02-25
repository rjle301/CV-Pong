import pygame

class Ball:
    def __init__(self, x_pos, y_pos, radius):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.diameter = radius * 2
        
        self.velocity_y = .2
        self.velocity_x = .2

    def get_x(self):
        return self.x_pos
    
    def get_y(self):
        return self.y_pos
    
    def get_radius(self):
        return self.radius
    
    def get_diameter(self):
        return self.diameter
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.x_pos, self.y_pos), self.radius, 0)
    
    def move(self):
        self.x_pos += self.velocity_x
        self.y_pos += self.velocity_y

    def flip_x_velocity(self):
        self.velocity_x *= -1
    
    def flip_y_velocity(self):
        self.velocity_y *= -1


class Paddle:
    def __init__(self, x_pos, y_pos, width, height):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.xPos = x_pos
        self.width = width
        self.height = height

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)

    def set_y(self, y_pos):
        self.rect.update(self.xPos, y_pos, self.width, self.height)

    def get_rectangle(self):
        return self.rect
