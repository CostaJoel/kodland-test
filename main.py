import pygame
import random
import sys
import os
root_path = os.path.abspath(os.path.split(__file__)[0])
sys.path.insert(0, os.path.join(root_path, 'kodland-test'))
sys.path.insert(0, root_path)
from src.Enemy import Enemy
from src.settings import BLACK, WHITE, WIDTH, HEIGHT
from src.Player import Player


def main_menu(screen, font):
    while True:
        screen.fill(BLACK)
        menu_text = font.render("Press Enter to Start", True, WHITE)
        screen.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 2 - menu_text.get_height() // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

def game_loop(screen, font):
    global enemies, score
    enemies = []
    score = 0
    
    clock = pygame.time.Clock()
    spawn_enemy_event = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_enemy_event, 1000)  # Spawn enemies every second
    
    player = Player()
    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                if event.key == pygame.K_SPACE:
                    player.prepare_bullet()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()

        if random.random() < 0.03:  # 2% chance to spawn an enemy
            enemies.append(Enemy())

        for enemy in enemies:
            is_enemy_wins = enemy.move()
            if is_enemy_wins:
                score -= 1
                enemies.remove(enemy)

        score = player.shoot(enemies=enemies, score=score)

        if player.pos[0] < 0:
            player.pos[0] = 0
        if player.pos[0] > WIDTH - player.size[0]:
            player.pos[0] = WIDTH - player.size[0]


        player.draw_player(screen)
        for enemy in enemies:
            enemy.draw_enemy(screen)
        player.draw_bullets(screen=screen)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)  # Frame rate


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kodland Space Invader")
    font = pygame.font.Font(None, 36)
    main_menu(screen=screen, font=font)
    game_loop(screen=screen, font=font)
