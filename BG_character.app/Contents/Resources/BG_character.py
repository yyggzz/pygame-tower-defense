import pygame
import os
pygame.init()


WIDTH, HEIGHT = 800, 400
CHARACTER_WIDTH, CHARACTER_HEIGHT = 64, 64
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Moving Character")

# Load images of the character
STATIONARY = pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/standing.png")
# One way to do it - using the sprites that face left.
LEFT =  [pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L1.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L2.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L3.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L4.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L5.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L6.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L7.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L8.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L9.png")]
# Another (faster) way to do it - using the sprites that face right.
RIGHT = [None]*10
for picIndex in range(1, 10):
    RIGHT[picIndex - 1] = pygame.image.load(os.path.join("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero", "R" + str(picIndex) + ".png"))

BG_IMG = pygame.image.load('/Users/yigezhang/Documents/CS/Pygame/defense_game/Background.png')
BG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))

BLACK = (0, 0, 0)


class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = 10
        self.vely = 10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        self.jump = False

    def move_hero(self, userInput):
        if userInput[pygame.K_LEFT] and self.x >= 0:
            self.face_left = True
            self.face_right = False
            self.x -= self.velx

        elif userInput[pygame.K_RIGHT] and self.x <= WIDTH - CHARACTER_WIDTH:
            self.face_right = True
            self.face_left = False
            self.x += self.velx

        else:
            self.stepIndex = 0

    def draw(self, WIN):
        if self.stepIndex >= 9:
            self.stepIndex = 0

        if self.face_left:
            WIN.blit(LEFT[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        elif self.face_right:
            WIN.blit(RIGHT[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1

    def jump_motion(self, userInput):
        if userInput[pygame.K_SPACE] and not self.jump:
            self.jump = True
        if self.jump:
            self.y -= self.vely
            self.vely -= 1
            if self.vely < -10:
                self.vely = 10
                self.jump = False



def draw_game():
    WIN.fill(BLACK)
    WIN.blit(BG, (0, 0))

    player.draw(WIN)

    pygame.time.delay(30) # higher value -> moves slower
    pygame.display.update()
    
player = Hero(250, 290)
# Main loop
run = True
while run:

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()

    # User input
    userInput = pygame.key.get_pressed()

    # Movement
    player.move_hero(userInput)
    player.jump_motion(userInput)

    # draw
    draw_game()


    
    
    


