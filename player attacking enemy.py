import pygame, sys

pygame.init()

display = pygame.display.set_mode((700,700))

class Player:
    def __init__(self,x,y,width,height,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    def draw(self):
        pygame.draw.rect(display,(250,0,0),(self.x,self.y,self.width,self.height))
    def move(self, keys):
        if keys[pygame.K_d] and self.x + self.width < 700:
            self.x += self.speed
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.speed

class Enemy:
    def __init__(self,x,y,width,height,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    def draw(self):
        pygame.draw.rect(display,(0,0,250),(self.x,self.y,self.width,self.height))
    def move(self):
        self.x+=self.speed
        if self.x <= 0 or self.x + self.width >= 700:
            self.speed = -self.speed

class Bullet:
    def __init__(self,x,y,width,height,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    def draw(self):
        pygame.draw.rect(display,(0,0,0),(self.x,self.y,self.width,self.height))
        self.y+=self.speed
        
player = Player(20,20,60,60,20)
enemy = Enemy(20,600,60,60,21)
b = Bullet(player.x+25,player.y,5,10,20)
bullets = []


running=True

while running:
    #event and bullet handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(Bullet(player.x + player.width // 2, player.y, 5, 10, 10))
            
    
    #player movement
    keys = pygame.key.get_pressed()
    player.move(keys)

        

    #enemy movement   
    enemy.move()
    

    display.fill((250,250,250))
    bullets.append(b)

    for bullet in bullets[:]:
        bullet.draw()
        if bullet.y <0:
            bullets.remove(bullet)  
            
    player.draw()
    enemy.draw()
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
pygame.quit()

"""
-----------------------------OLD CODE---------------------------------------
player = pygame.Rect((20,20,60,60))
player_speed = 100
enemy = pygame.Rect((20,600,60,60))
pygame.draw.rect(display,(250,0,0),player)
pygame.draw.rect(display,(0,0,250),enemy)
#bullet = Bullet(player.x+25,player.y,5,10,20)
#if keys[pygame.K_SPACE]:
        #bullets.append(Bullet(player.x + player.width // 2, player.y, 5, 10, 10))

"""
