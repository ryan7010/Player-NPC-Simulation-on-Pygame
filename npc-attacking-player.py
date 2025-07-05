import pygame, sys

pygame.init()

display = pygame.display.set_mode((700,700))

class NPC:
    def __init__(self,x,y,width,height,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    def draw(self):
        pygame.draw.rect(display,(250,0,0),(self.x,self.y,self.width,self.height))
    def move(self,px):
        if self.x<px:
            self.x+=self.speed
        elif self.x>px:
            self.x-=self.speed
        

class Player:
    def __init__(self,x,y,width,height,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    def draw(self):
        pygame.draw.rect(display,(0,0,250),(self.x,self.y,self.width,self.height))
    def move(self, keys):
        if keys[pygame.K_d] and self.x + self.width < 700:
            self.x += self.speed
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.speed

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
        
player = Player(20,600,60,60,20)
npc = NPC(20,20,60,60,3)
b = Bullet(player.x+25,player.y,5,10,20)
bullets = []

last_shot = pygame.time.get_ticks()

running=True

while running:
    #event and bullet handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #bullets.append(Bullet(npc.x + npc.width // 2, npc.y, 5, 10, 10))
            
    
    #player movement
    keys = pygame.key.get_pressed()
    player.move(keys)
    npc.move(player.x)    

    current_time = pygame.time.get_ticks()
    if current_time - last_shot > 500:
        bullets.append(Bullet(npc.x + npc.width // 2, npc.y + npc.height, 5, 10, 10))
        last_shot = current_time


    display.fill((250,250,250))

    for bullet in bullets[:]:
        bullet.draw()
        if bullet.y > 700:
            bullets.remove(bullet)
        if player.x <= bullet.x <= player.x + player.width and player.y <= bullet.y <= player.y + player.height:
            running = False
    #print(f'BulletX:{bullet.x} BulletY:{bullet.y} PlayerX:{player.x} Player Y:{player.y}')
            
    player.draw()
    npc.draw()
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
