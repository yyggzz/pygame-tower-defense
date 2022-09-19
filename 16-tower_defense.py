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

# Load sound effects
MUSIC = pygame.mixer.music.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/music.ogg")
POP_SOUND = pygame.mixer.Sound("/Users/yigezhang/Documents/CS/Pygame/defense_game/pop.ogg")
pygame.mixer.music.play(-1)

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

# Load image of tower
TOWER_IMG = pygame.transform.scale(pygame.image.load("/Users/yigezhang/Documents/CS/Pygame/defense_game/Tower.png"), (200, 200))

# Load image of background
BG_IMG = pygame.image.load('/Users/yigezhang/Documents/CS/Pygame/defense_game/Background.png')
BG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

FONT_HEALTH = pygame.font.Font("freesansbold.ttf", 28)

VEL_BULLET = 15
VEL_HERO = 10
DIR_LEFT = -1 # direct to left
DIR_RIGHT = 1 # direct to right
hit_count = 0

enemy_speed = 3
enemy_killed = 0
# Tower
tower_health = 5

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = VEL_HERO
        self.vely = VEL_HERO
        self.direction = DIR_RIGHT
        self.stepIndex = 0
        self.jump = False
        # Bullet
        self.bullets = []
        self.cool_down_count = 0
        # Health
        self.hitbox = pygame.Rect(self.x, self.y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
        self.health = 30
        self.lives = 1
        self.alive = True

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
        #pygame.draw.rect(WIN, BLACK, (self.x + 20, self.y + 15, CHARACTER_WIDTH - 40, CHARACTER_HEIGHT - 15), 1)
        self.hitbox =  pygame.Rect(self.x + 20, self.y + 15, CHARACTER_WIDTH - 40, CHARACTER_HEIGHT - 15)

        # Draw health bar of hero
        pygame.draw.rect(WIN, RED, (self.x + 15, self.y, 30, 5))
        if self.health >= 0:
            pygame.draw.rect(WIN, GREEN, (self.x + 15, self.y, self.health, 5))

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
        self.hit()
        self.cooldown()
        if userInput[pygame.K_f] and self.cool_down_count == 0:
            POP_SOUND.play()
            bullet = Bullet(self.x, self.y, self.direction)
            self.bullets.append(bullet)
            self.cool_down_count = 1

        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def hit(self): # bullet hits enemy
        for enemy in enemies:
            for bullet in self.bullets:
                if pygame.Rect.colliderect(bullet.hitbox, enemy.hitbox):
                    print("Bullet hit enemy!")
                    self.bullets.remove(bullet)
                    enemy.health -= 10
                    

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x + 15
        self.y = y + 25
        self.direction = direction
        # hitbox
        self.hitbox = pygame.Rect(self.x, self.y, BULLET_WIDTH, BULLET_HEIGHT)

    def draw_bullet(self):
        self.hitbox = pygame.Rect(self.x, self.y, BULLET_WIDTH, BULLET_HEIGHT)
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
    def __init__(self, x, y, direction, speed):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.stepIndex = 0
        # Hitbox
        self.hitbox = pygame.Rect(self.x, self.y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
        self.health = 30

    def draw(self):
        #pygame.draw.rect(WIN, BLACK, (self.x + 15, self.y + 5, CHARACTER_WIDTH - 25, CHARACTER_HEIGHT - 10), 1)
        self.hitbox = pygame.Rect(self.x + 15, self.y + 5, CHARACTER_WIDTH - 25, CHARACTER_HEIGHT - 10) # add some adjustments to the real size of character

        # Draw health bar of enemy
        pygame.draw.rect(WIN, RED, (self.x + 15, self.y, 30, 5))
        if self.health >= 0:
            pygame.draw.rect(WIN, GREEN, (self.x + 15, self.y, self.health, 5))

        if self.direction == DIR_LEFT:
            WIN.blit(LEFT_ENEMY[self.stepIndex//3], (self.x, self.y))
        elif self.direction == DIR_RIGHT:
            WIN.blit(RIGHT_ENEMY[self.stepIndex//3], (self.x, self.y))
        self.stepIndex += 1
        if self.stepIndex > 30:
            self.stepIndex = 0

    def move(self):
        self.hit()
        if self.direction == DIR_LEFT:
            self.x -= self.speed
        elif self.direction == DIR_RIGHT:
            self.x += self.speed

    def hit(self):
        if pygame.Rect.colliderect(self.hitbox, player.hitbox):
            print("Enemy hit player!")
            if player.health > 0:
                player.health -= 1
                if player.lives > 0 and player.health == 0:
                    player.lives -= 1
                    player.health = 30
                elif player.lives == 0 and player.health == 0:
                    player.alive = False

    def off_screen(self):
        return self.x < -ENEMY_WIDTH or self.x > WIDTH

def draw_game():
    global tower_health, enemy_killed, enemy_speed
    WIN.fill(BLACK)
    WIN.blit(BG, (0, 0))

    # Draw player
    player.draw()

    # Draw bullets
    for bullet in player.bullets:
        bullet.draw_bullet()
    
    # Draw enemies
    for enemy in enemies:
        enemy.draw()

    # Draw tower
    WIN.blit(TOWER_IMG, (-50, 170))

    # Draw player lives
    if not player.alive:
        WIN.fill(WHITE)
        newgame_text = FONT_HEALTH.render("You died! Press 'R' to restart.", True, BLACK)
        enemies.clear()
        WIN.blit(newgame_text, (WIDTH//2 - newgame_text.get_width()//2, HEIGHT//2 - newgame_text.get_height()))
        if userInput[pygame.K_r]:
            player.alive = True
            player.lives = 1
            player.health = 30
            tower_health = 5
            enemy_speed = 3
            enemy_killed = 0
            
    else:
        health_text = FONT_HEALTH.render("Lives: " + str(player.lives) + " | Tower health: " + str(tower_health) + " | Kills: " + str(enemy_killed), True, BLACK)
        WIN.blit(health_text, (WIDTH//2 - health_text.get_width()//2, 20))

    # Time delay and update
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

    # Tower health
    if tower_health == 0:
        player.alive = False

    # Enemy
    if len(enemies) == 0:
        enemy = Enemy(WIDTH - ENEMY_WIDTH, 300, DIR_LEFT, enemy_speed)
        enemies.append(enemy)
        if enemy_speed <= 10:
            enemy_speed += 1

    for enemy in enemies:
        enemy.move()
        if enemy.off_screen():
            enemies.remove(enemy)
        
        if enemy.x < 50:
            enemies.remove(enemy)
            tower_health -= 1
        
        if enemy.health <= 0:
            enemy_killed += 1
            enemies.remove(enemy)

    # draw
    draw_game()


    
    
    


