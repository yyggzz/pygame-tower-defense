import pygame
import os


WIDTH, HEIGHT = 500, 500
CHARACTER_WIDTH, CHARACTER_HEIGHT = 64, 64
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Character")

# Load images of the character
STATIONARY = pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/standing.png")
# One way to do it - using the sprites that face left.
LEFT =  [pygame.image.load(os.path.join("Hero", "L1.png")),
         pygame.image.load(os.path.join("Hero", "L2.png")),
         pygame.image.load(os.path.join("Hero", "L3.png")),
         pygame.image.load(os.path.join("Hero", "L4.png")),
         pygame.image.load(os.path.join("Hero", "L5.png")),
         pygame.image.load(os.path.join("Hero", "L6.png")),
         pygame.image.load(os.path.join("Hero", "L7.png")),
         pygame.image.load(os.path.join("Hero", "L8.png")),
         pygame.image.load(os.path.join("Hero", "L9.png"))]

# Another (faster) way to do it - using the sprites that face right.
RIGHT = [None]*10
for picIndex in range(1, 10):
    RIGHT[picIndex - 1] = pygame.image.load(os.path.join("Hero", "R" + str(picIndex) + ".png"))


BLACK = (0, 0, 0)

x, y = WIDTH//2 - CHARACTER_WIDTH//2, HEIGHT//2 - CHARACTER_HEIGHT//2
VEL = 10

MOVE_LEFT, MOVE_RIGHT = False, False
stepIndex = 0

def draw_game():
    WIN.fill(BLACK)
    global stepIndex
    if stepIndex >= 9:
        stepIndex = 0

    if MOVE_LEFT:
        WIN.blit(LEFT[stepIndex], (x, y))
        stepIndex += 1
    elif MOVE_RIGHT:
        WIN.blit(RIGHT[stepIndex], (x, y))
        stepIndex += 1
    else:
        WIN.blit(STATIONARY, (x, y))



# Main loop
run = True
while run:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

    draw_game()

    # Movement
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and x >= 0:
        x -= VEL
        MOVE_LEFT = True
        MOVE_RIGHT = False

    elif keys_pressed[pygame.K_RIGHT] and x <= WIDTH - CHARACTER_WIDTH:
        x += VEL
        MOVE_LEFT = False
        MOVE_RIGHT = True

    else:
        MOVE_LEFT = False
        MOVE_RIGHT = False
        stepIndex = 0
    
    pygame.time.delay(30) # higher value -> moves slower
    pygame.display.update()


