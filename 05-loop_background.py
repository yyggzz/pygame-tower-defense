import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("looping background")
BG_IMG = pygame.image.load('/Users/yigezhang/Documents/CS/Pygame/defense_game/Background.png')
BG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))

FPS = 60
i = 0
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    WIN.blit(BG, (i, 0))
    WIN.blit(BG, (i + WIDTH, 0))
    if i == -WIDTH:
        i = 0
    i -= 1

    pygame.display.update()