import pygame

class Paddle:
    def __init__(self, x_pos, y_pos, width, height):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.xPos = x_pos

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)

    def setY(self, y_pos):
        self.rect = self.rect.move(self.xPos, y_pos)
    