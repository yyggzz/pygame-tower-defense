import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump circle")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

x, y = WIDTH//2, HEIGHT//2
RADIUS = 15
VEL_x = 10
VEL_Y_MAX = 10
VEL_y = VEL_Y_MAX
jump = False

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
    if keys_pressed[pygame.K_LEFT] and x >= 0 + RADIUS + VEL_x:
        x -= VEL_x
    if keys_pressed[pygame.K_RIGHT] and x <= WIDTH - RADIUS - VEL_x:
        x += VEL_x

    if not jump and keys_pressed[pygame.K_SPACE]:
        jump = True
    if jump:
        y -= VEL_y
        VEL_y -= 1
        if VEL_y < -VEL_Y_MAX:
            jump = False
            VEL_y = VEL_Y_MAX


        
    

    pygame.display.update()