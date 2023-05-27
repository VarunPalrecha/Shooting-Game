import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooting Game")

# Load the forest background image
background = pygame.image.load("forest_background.png").convert()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player parameters
player_width = 50
player_height = 50
player_speed = 5

# Create the player
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (player_width, player_height))
player_rect = player_img.get_rect()
player_rect.centerx = width // 2
player_rect.bottom = height - 10

# Bullet parameters
bullet_width = 10
bullet_height = 30
bullet_speed = 10

# Create bullets
bullet_img = pygame.Surface((bullet_width, bullet_height))
bullet_img.fill(RED)
bullet_rect = bullet_img.get_rect()
bullet_rect.centerx = player_rect.centerx
bullet_rect.centery = player_rect.top

bullets = []

# Enemy parameters
enemy_width = 50
enemy_height = 50
enemy_speed = 3

# Create enemies
enemy_img = pygame.image.load("enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (enemy_width, enemy_height))
enemy_rect = enemy_img.get_rect()
enemy_rect.x = random.randint(0, width - enemy_width)
enemy_rect.y = 0

enemies = []

# Game loop
screen.blit(background, (0, 0))
running = True
clock = pygame.time.Clock()

while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shoot bullets when spacebar is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet_rect = bullet_img.get_rect()
            bullet_rect.centerx = player_rect.centerx
            bullet_rect.centery = player_rect.top
            bullets.append(bullet_rect)

    # Process user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    # Update game state
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    enemy_rect.y += enemy_speed

    if enemy_rect.y > height:
        enemy_rect.x = random.randint(0, width - enemy_width)
        enemy_rect.y = 0

    # Check for collisions
    for bullet in bullets:
        if bullet.colliderect(enemy_rect):
            bullets.remove(bullet)
            enemy_rect.x = random.randint(0, width - enemy_width)
            enemy_rect.y = 0

    if player_rect.colliderect(enemy_rect):
        running = False

    # Render graphics
    screen.fill(WHITE)
    screen.blit(player_img, player_rect)
    screen.blit(enemy_img, enemy_rect)

    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

# Game over
font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over", True, RED)
game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()



# Wait for a few seconds before quitting
pygame.time.wait(2000)

# Quit the game
pygame.quit()
