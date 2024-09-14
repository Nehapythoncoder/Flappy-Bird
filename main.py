import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()
fps = 60 

sceenn_width = 864
screen_heigth = 936
pygame.dislpay.set_caption("Flappy Bird")
pygame.display.set_mode((screen_width,screen_heigth))

#load font
font = pygame.font.Sysfont("Bauhaus 93",60)

white = (255,255,255)

#game variables
ground_scroll = 0 
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks()-pipe_frequency
score = 0 
pass_pipe = False

#load images
bg = pygame.image.load("img/Bg.png")
ground_img = pygame.image.load("img/Ground.png")
button_img = pygame.image.load("img/Restart.png")

def draw_text(text,col,x,y):
    txt = font.render(text,True,col)
    screen.blit(txt,(x,y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_heigth/2)
    score = 0 
    return score

class Bird(pygame.sprite.Sprite)
    def __init__(self,x,y)
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        self.index = 0 
        self.counter = 0
        for num in range(1,4):
            img = pygame.image.load(f"img/bird{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.clicked = False

    def update(self):
        if flying == True:
            #apply Gravity
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom <768:
                self.rect.y +=int(self.vel)

        if game_over == False:
            #jump
            if pygame.mouse.get_pressed()[0]== 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10 
            if pygame.mouse.get_presssed()[0] == 0:
                self.clicked = False

            # handle animation
            flap_cooldown = 5 
            self.counter += 1 
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1 
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
              
            #rotate the bird
            self.image = pygame.transform.rotate(self.images[self.index],self.vel*-2)
            
        else:
            #point to the ground
            self.imag = pygame.transform.rotate(self.images[self.index],-90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.images = pygame.image.load("img/pipe.png")
        self.rect = self.image.get_rect()

        #position variable is 1 it will vome from the top, -1 then it will come from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y-int(pipe_gap/2)]
        elif position == -1:
            self.rect.topleft = [x,y-int(pipe_gap/2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
         self.kill()

class Button():
    def __init__(self,x,y,image):
        self.image = image 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False 

        #get mouse pos
        pos = pygame.mouse.get_pos()
        #check if mouseover or clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True 

        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action  
    
pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()

flappy = Bird(100,int(screen_height/2))
bird_group.add(flappy)

button = Button(screen_width//2 - 50 ,screen_height//2 - 100,button_img)

run = True
while run:
    clock.tick(fps)

    screen.blit(bg,(0,0))

    pipe_group.draw(screen)
    bird_group.draw(screen)
    bird_group.update()

    screen.blit(ground_img,(ground_scroll,768)) 

    #check the score 
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and pass_pipe == False:
            pass_pipe = True
        if bird_group.sprites()[0].rect.left . pipe_group.sprites()[0].rect.right:
            score = score+1
            pass_pipe  = False

    draw_text(str(score),font,white,int(screen_width/2),20)


