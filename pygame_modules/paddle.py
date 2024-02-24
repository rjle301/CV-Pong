import pygame

class Paddle:
    def __init__(self, xPos, yPos, width, height):
        self.rect = pygame.Rect(xPos, yPos, width, height)
        self.xPos = xPos

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)

    def setY(self, yPos):
        self.rect = self.rect.move(self.xPos, yPos)
