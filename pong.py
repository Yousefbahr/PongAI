import pygame

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)


# Set screen
pygame.init()
HEIGHT, WIDTH, SIZE = 35, 30, 20
screen = pygame.display.set_mode((HEIGHT * SIZE, WIDTH * SIZE))
FPS = 30
clock = pygame.time.Clock()
background = pygame.Surface((HEIGHT * SIZE, WIDTH * SIZE))
background.fill(black)

# Set game
player1 = [(0, 0), (0, 1), (0, 2), (0, 3)]

EXIT = False

while True:
    direction = (0, 0)

    if EXIT:
        break

    clock.tick(FPS)
    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Down
    if keys[pygame.K_s]:
        direction = (0, 1)
    # UP
    if keys[pygame.K_w]:
        direction = (0, -1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EXIT = True

    screen.blit(background, (0, 0))

    # Change player1 coordinates
    for i, coord in enumerate(player1):
        player1[i] = (coord[0] + direction[0], coord[1] + direction[1])

    # Draw player1
    for i, position in enumerate(player1):
        pygame.draw.rect(screen, white, (position[0] * SIZE, position[1] * SIZE, SIZE, SIZE))

    pygame.display.flip()









