import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
BALL_SIZE = 30
PLAYER_COLOR = (0, 128, 255)
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
PLAYER_SPEED = 5
BALL_SPEED = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Ball")

player_x = (WIDTH - PLAYER_SIZE) // 2
player_y = HEIGHT - PLAYER_SIZE - 20


ball_x = random.randint(0, WIDTH - BALL_SIZE)
ball_y = 0

running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += PLAYER_SPEED

    ball_y += BALL_SPEED

    if player_x < ball_x + BALL_SIZE and player_x + PLAYER_SIZE > ball_x:
        if player_y < ball_y + BALL_SIZE and player_y + PLAYER_SIZE > ball_y:

            score += 1
            ball_x = random.randint(0, WIDTH - BALL_SIZE)
            ball_y = 0

    window.fill(BACKGROUND_COLOR)
    pygame.draw.rect(window, PLAYER_COLOR, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.ellipse(window, BALL_COLOR, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    pygame.display.update()

pygame.quit()
