import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move circle")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

x, y = WIDTH//2, HEIGHT//2
RADIUS = 15
VEL = 10


run = True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)

    WIN.fill(BLACK)

    pygame.draw.circle(WIN, WHITE, (x, y), RADIUS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and x >= 0 + RADIUS + VEL:
        x -= VEL
    if keys_pressed[pygame.K_RIGHT] and x <= WIDTH - RADIUS - VEL:
        x += VEL
    if keys_pressed[pygame.K_UP] and y >= 0 + RADIUS + VEL:
        y -= VEL
    if keys_pressed[pygame.K_DOWN] and y <= HEIGHT - RADIUS - VEL:
        y += VEL    
        
    

    pygame.display.update()