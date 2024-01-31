import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Frogger")

# Set up the clock
clock = pygame.time.Clock()

# Set up the frog
frog_image = pygame.image.load("frog.png")
frog_rect = frog_image.get_rect()
frog_speed = 5

# Set up the obstacles
obstacle_images = [pygame.image.load("car.png"), pygame.image.load("log.png")]
obstacle_rects = []
obstacle_speeds = [3, 2]
obstacle_spawn_rate = 100

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the frog's position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        frog_rect.y -= frog_speed
    if keys[pygame.K_DOWN]:
        frog_rect.y += frog_speed
    if keys[pygame.K_LEFT]:
        frog_rect.x -= frog_speed
    if keys[pygame.K_RIGHT]:
        frog_rect.x += frog_speed

    # Spawn obstacles
    if random.randint(0, obstacle_spawn_rate) == 0:
        obstacle_rect = obstacle_images[random.randint(0, len(obstacle_images) - 1)].get_rect()
        obstacle_rect.x = screen_width
        obstacle_rects.append(obstacle_rect)

    # Move obstacles
    for i, obstacle_rect in enumerate(obstacle_rects):
        obstacle_rect.x -= obstacle_speeds[i % len(obstacle_speeds)]
        if obstacle_rect.x < 0:
            obstacle_rects.pop(i)

    # Check for collisions
    for obstacle_rect in obstacle_rects:
        if frog_rect.colliderect(obstacle_rect):
            running = False

    # Update the score
    if frog_rect.x > screen_width - frog_rect.width:
        score += 1

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(frog_image, frog_rect)
    for obstacle_rect in obstacle_rects:
        screen.blit(random.choice(obstacle_images), obstacle_rect)
    text = font.render("Score: {}".format(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()