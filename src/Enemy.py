import pygame
from src.settings import RED, HEIGHT, WIDTH
import random

class Enemy:
    
    def __init__(self, size = (50,30), speed=5, color=RED):
        # Enemy settings
        self.size = size
        self.speed = speed
        self.pos = [random.randint(0, WIDTH - size[0]), 0]
        self.color = color


    def move(self):
        self.pos[1] += self.speed
        if self.pos[1] > HEIGHT:
            return True


    def draw_enemy(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]))