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
ground_img = pygame.image.load(img/Ground.png)
button_img = pygame.image.load(img/Restart.png)

def draw_text(text,col,x,y):
    txt = font.render(text,True,col)
    screen.blit(txt,(x,y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_heigth/2)
    score =
