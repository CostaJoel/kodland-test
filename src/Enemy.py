import pygame
from src.settings import RED, HEIGHT, WIDTH
import random

class Enemy:
    
    def __init__(self, size = (40,40), speed=5, color=RED):
        # Enemy settings
        self.size = size
        self.speed = speed
        self.pos = [random.randint(0, WIDTH - size[0]), 0]
        self.color = color
        self.enemy_image = pygame.image.load('assets/enemy.png')
        self.enemy_image = pygame.transform.scale(self.enemy_image, (40, 40))
        pass


    def move(self):
        self.pos[1] += self.speed
        if self.pos[1] > HEIGHT:
            return True


    def draw_enemy(self, screen):
        screen.blit(self.enemy_image, (self.pos[0], self.pos[1]))