import pygame
import os
pygame.init()


WIDTH, HEIGHT = 800, 400
CHARACTER_WIDTH, CHARACTER_HEIGHT = 64, 64
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Moving Character Shooting")

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
BULLET_IMG = pygame.transform.scale(pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/light_bullet.png"), (10, 10))

BLACK = (0, 0, 0)
VEL_BULLET = 15

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
        # bullet
        self.bullets = []
        self.cool_down_count = 0

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

    def direction(self):
        if self.face_right:
            return 1
        elif self.face_left:
            return -1

    def cooldown(self):
        if self.cool_down_count >= 10:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        self.cooldown()
        if userInput[pygame.K_f] and self.cool_down_count == 0:
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1

        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x + 15
        self.y = y + 25
        self.direction = direction

    def draw_bullet(self):
        WIN.blit(BULLET_IMG, (self.x, self.y))

    def move(self):
        if self.direction == 1:
            self.x += VEL_BULLET
        if self.direction == -1:
            self.x -= VEL_BULLET

    def off_screen(self):
        if self.x < -10 or self.x > WIDTH:
            return True


def draw_game():
    WIN.fill(BLACK)
    WIN.blit(BG, (0, 0))

    player.draw(WIN)

    for bullet in player.bullets:
        bullet.draw_bullet()

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

    # Shoot
    player.shoot()

    # Movement
    player.move_hero(userInput)
    player.jump_motion(userInput)

    # draw
    draw_game()


    
    
    


