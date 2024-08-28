import pygame
from src.settings import player_size, bullet_size, bullets, bullet_speed, WIDTH, HEIGHT, WHITE, GREEN


class Player:
    

    def __init__(self, size = (50,50), speed=10, color=GREEN) -> None:
        self.size = size
        self.speed = speed
        self.pos = [WIDTH // 2, HEIGHT - 2 * player_size[1]]
        self.color = color
        self.bullets = []
        self.player_image = pygame.image.load('assets/player.png')
        self.player_image = pygame.transform.scale(self.player_image, (50, 50))
        pass

    


    def draw_player(self, screen):
        screen.blit(self.player_image, (self.pos[0], self.pos[1]))


    def move_left(self):
        self.pos[0] -= self.speed


    def move_right(self):
        self.pos[0] += self.speed

    
    def prepare_bullet(self):
        self.bullets.append([self.pos[0] + self.size[0] // 2 - bullet_size[0] // 2, self.pos[1]])


    def _draw_bullet(self, screen, bullet_pos):
        pygame.draw.rect(screen, WHITE, pygame.Rect(bullet_pos[0], bullet_pos[1], bullet_size[0], bullet_size[1]))


    def draw_bullets(self, screen):
        for bullet in self.bullets:
            self._draw_bullet(screen, bullet)


    def shoot(self, enemies, score):
        for bullet in self.bullets:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                del bullet
            else:
                for enemy in enemies:
                    if (bullet[0] < enemy.pos[0] + enemy.size[0] and
                        bullet[0] + bullet_size[0] > enemy.pos[0] and
                        bullet[1] < enemy.pos[1] + enemy.size[1] and
                        bullet[1] + bullet_size[1] > enemy.pos[1]):
                        enemies.remove(enemy)
                        del bullet
                        score += 1
                        break
        return score