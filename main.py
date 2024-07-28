import pygame
import sys
import random

# Initializing Pygame
pygame.init()

# Setting up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Setting up colors
white = (255, 255, 255)

# Setting up the bird
bird_size = 50
bird_x = width // 4
bird_y = height // 2 - bird_size // 2
bird_velocity = 0
gravity = 1

# Setting up the pipes
pipe_width = 100
pipe_height = random.randint(100, 400)
pipe_x = width
pipe_gap = 150
pipe_speed = 5

# Setting up the game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -15  # Jump

    # Updating bird position and velocity
    bird_y += bird_velocity
    bird_velocity += gravity

    # Updating pipe position
    pipe_x -= pipe_speed
    if pipe_x < 0:
        pipe_x = width
        pipe_height = random.randint(100, 400)

    # To check for collisions
    if (
        bird_x < pipe_x + pipe_width
        and bird_x + bird_size > pipe_x
        and (bird_y < pipe_height or bird_y + bird_size > pipe_height + pipe_gap)
    ):
        # Game over
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Clearing screen
    screen.fill(white)

    # Draw bird
    pygame.draw.rect(screen, (255, 0, 0), (bird_x, bird_y, bird_size, bird_size))

    # Draw pipes
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(
        screen,
        (0, 255, 0),
        (pipe_x, pipe_height + pipe_gap, pipe_width, height - (pipe_height + pipe_gap)),
    )

    # Updating the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)
