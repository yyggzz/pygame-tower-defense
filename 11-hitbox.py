import pygame
import os
import random
pygame.init()


WIDTH, HEIGHT = 800, 400
CHARACTER_WIDTH, CHARACTER_HEIGHT = 64, 64
ENEMY_WIDTH, ENEMY_HEIGHT = 64, 64
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Moving Character Shooting enemy")

# Load images of the hero
LEFT_HERO =  [pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L1.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L2.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L3.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L4.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L5.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L6.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L7.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L8.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/L9.png")]
RIGHT_HERO = [pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/R1.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/R2.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/R3.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/R4.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/R5.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/R6.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/R7.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/R8.png"),
         pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Hero/R9.png")] 
# Load images of the enemy
LEFT_ENEMY = [pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/L1E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/L2E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/L3E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/L4E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/L5E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/L6E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/L7E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/L8E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/L9P.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/L10P.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/L11P.png")]
RIGHT_ENEMY = [pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/R1E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/R2E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/R3E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/R4E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/R5E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/R6E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/R7E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/R8E.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/R9P.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/R10P.png"),
              pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Enemy/R11P.png")]

# Load image of bullet            
BULLET_IMG = pygame.transform.scale(pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/light_bullet.png"), (10, 10))
BULLET_WIDTH, BULLET_HEIGHT = 10, 10

# Load image of background
BG_IMG = pygame.image.load('/Users/yigezhang/Documents/CS/Pygame/defense_game/Background.png')
BG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))

BLACK = (0, 0, 0)
VEL_BULLET = 15
VEL_HERO = 10
DIR_LEFT = -1 # direct to left
DIR_RIGHT = 1 # direct to right

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = VEL_HERO
        self.vely = VEL_HERO
        self.direction = DIR_RIGHT
        self.stepIndex = 0
        self.jump = False
        # bullet
        self.bullets = []
        self.cool_down_count = 0
        # Health
        self.hitbox = (self.x, self.y, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    def move_hero(self, userInput):
        if userInput[pygame.K_LEFT] and self.x >= 0:
            self.direction = DIR_LEFT
            self.x -= self.velx

        elif userInput[pygame.K_RIGHT] and self.x <= WIDTH - CHARACTER_WIDTH:
            self.direction = DIR_RIGHT
            self.x += self.velx

        else:
            self.stepIndex = 0

    def draw(self):
        self.hitbox = (self.x + 20, self.y + 15, CHARACTER_WIDTH - 40, CHARACTER_HEIGHT - 15) # add some adjustments to the real size of character
        pygame.draw.rect(WIN, BLACK, self.hitbox, 1)

        if self.stepIndex >= 9:
            self.stepIndex = 0

        if self.direction == DIR_LEFT:
            WIN.blit(LEFT_HERO[self.stepIndex], (self.x, self.y))
        elif self.direction == DIR_RIGHT:
            WIN.blit(RIGHT_HERO[self.stepIndex], (self.x, self.y))
        self.stepIndex += 1

    def jump_motion(self, userInput):    
        if userInput[pygame.K_SPACE] and not self.jump:
            self.jump = True
        if self.jump:
            self.y -= self.vely * 2
            self.vely -= 1
            if self.vely < -VEL_HERO:
                self.vely = VEL_HERO
                self.jump = False

    def cooldown(self):
        if self.cool_down_count >= 10:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        self.cooldown()
        if userInput[pygame.K_f] and self.cool_down_count == 0:
            bullet = Bullet(self.x, self.y, self.direction)
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
        if self.direction == DIR_RIGHT:
            self.x += VEL_BULLET
        if self.direction == DIR_LEFT:
            self.x -= VEL_BULLET

    def off_screen(self):
        if self.x < -BULLET_WIDTH or self.x > WIDTH:
            return True

class Enemy:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.stepIndex = 0
        # Health
        self.hitbox = (self.x, self.y, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    def draw(self):
        self.hitbox = (self.x + 15, self.y + 5, CHARACTER_WIDTH - 25, CHARACTER_HEIGHT - 10) # add some adjustments to the real size of character
        pygame.draw.rect(WIN, BLACK, self.hitbox, 1)

        if self.direction == DIR_LEFT:
            WIN.blit(LEFT_ENEMY[self.stepIndex//3], (self.x, self.y))
        elif self.direction == DIR_RIGHT:
            WIN.blit(RIGHT_ENEMY[self.stepIndex//3], (self.x, self.y))
        self.stepIndex += 1
        if self.stepIndex > 30:
            self.stepIndex = 0

    def move(self):
        if self.direction == DIR_LEFT:
            self.x -= 3
        elif self.direction == DIR_RIGHT:
            self.x += 3

    def off_screen(self):
        return self.x < -ENEMY_WIDTH or self.x > WIDTH

def draw_game():
    WIN.fill(BLACK)
    WIN.blit(BG, (0, 0))

    player.draw()

    for bullet in player.bullets:
        bullet.draw_bullet()
    
    for enemy in enemies:
        enemy.draw()

    pygame.time.delay(30) # higher value -> moves slower
    pygame.display.update()

# Instance of player class
player = Hero(250, 290)
# Instance of enemy class
enemies = []

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

    # Enemy
    if len(enemies) == 0:
        rand_no = random.randint(0, 1)
        if rand_no == 1:
            enemy = Enemy(WIDTH - ENEMY_WIDTH, 300, DIR_LEFT)
            enemies.append(enemy)
        if rand_no == 0:
            enemy = Enemy(0, 300, DIR_RIGHT)
            enemies.append(enemy)
    for enemy in enemies:
        enemy.move()
        if enemy.off_screen():
            enemies.remove(enemy)

    # draw
    draw_game()


    
    
    


