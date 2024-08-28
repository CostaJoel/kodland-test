WIDTH, HEIGHT = 800, 600
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Load assets (assuming you have the images in the assets folder)
# For simplicity, we'll use colored rectangles instead
player_color = GREEN
enemy_color = RED
# Player settings
player_size = (50, 30)
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size[1]]
player_speed = 10
# Bullet settings
bullet_color = WHITE
bullet_size = (10, 20)
bullets = []
bullet_speed = 20

