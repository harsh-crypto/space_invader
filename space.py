import pygame as pg
import time
import math as mt
from PIL import Image
import random
w = 1080
h = 720
wp = 540
run = True
'''
def screen():
    scrren.blit()
    screen.blit()
'''
pg.init()
RED_SHIP = pg.image.load(r"D:/code/red_enemy.png")
BLUE_SHIP = pg.image.load(r"d:/code/blue_enemy.png")
RED_LASER = pg.image.load(r"D:/code/red_laser.png")
BLUE_LASER = pg.image.load(r"D:/code/blue_laser.png")
COLOR_map = {
            "red" : (RED_SHIP,RED_LASER),
            "blue": (BLUE_SHIP,BLUE_LASER)
        }

class enemy:
    def __init__(self,x,y,color):
        self.health = 50
        self.image,self.lasers = COLOR_map[color]
        self.x = x
        self.y = y
    def draw(self):
        screen.blit(self.image,(self.x,self.y))


        '''
def bullet(x,y):
    screen.blit(pg.image.load(r"D:\code\laser.png"),(x,y))
'''
class player:
    def __init__(self,image,x,y):
        self.pos = [x,y]
        self.mask = None
        self.health = 100
        self.lives = 3
        self.lasers = pg.image.load(r"D:/code/red_laser.png")
        self.image = pg.image.load(image)
    def draw(self, m):
        x, y = self.pos
        screen.blit(self.image , (x+m,y))
        self.pos = [x+m,y]
        #self.mask = pg.mask.from_surface(self.image)
    def retposp(self,ps):
        x,y=self.pos
        if ps == "x":
            return x
        elif ps == "y":
            return y
    def get_live(self):
        return self.lives
color_code = random.randint(0,1)
image = Image.open(r"D:\code\background.jpg")
image.thumbnail((w,h))
image.save("background.jpg")
play1 = player(r"D:\code\Artboard 1spaceship.png",wp, h-100)
enmy = enemy(random.randint(0,(w-100)/2)*2,random.randint(0,h*0.25)*2,random.choice(["red","blue"]))
pg.display.set_caption("Space")
screen = pg.display.set_mode((w,h))
move = 0
b_m = 0
b=0
rows = 0
moveenmyX = 1
moveenmyY = 0
wavelenght = 10
main_font = pg.font.SysFont("Monutserrat",50)
enemies = []
for i in range(wavelenght):
    x,y = random.randrange(50,w-50) , -(random.randrange(0,500))
    enmy = enemy(x,y,random.choice(["red","blue"]))
    enemies.append(enmy)
while run:
    screen.fill((0,0,0))
    live_label = main_font.render(f"Lives:{play1.get_live()}",1,(255,255,255))
    lose = main_font.render(f"YOU LOSE",2,(255,255,255))
    screen.blit(pg.image.load("background.jpg"),(0,0))
    screen.blit(live_label , (10,10))
    play1.draw(move)    
    move = 0
    enmy.draw()   
    print(play1.pos[0],play1.pos[1])
    
    print("enemy: {0},{1},row: {2}".format(enmy.x,enmy.y,rows))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    K = pg.key.get_pressed()
    if K[pg.K_RIGHT] and play1.pos[0] != w-40:
        move = 10
    elif K[pg.K_LEFT] and play1.pos[0] != 20:
        move = -10

    if enmy.x == play1.pos[0] and enmy.y == play1.pos[1]:
        play1.dec_H(20)
        if play1.health ==0:
            play1.lives -=1
    if play1.lives <= 0:
        print("you Lose")
        screen.blit(lose,(int(w/2),int(h/2)))
    for enmy in enemies:
        enmy.draw()
        if enmy.y>h-5:
            play1.lives-=1
            enemies.remove(enmy)
        if enmy.x == play1.pos[0] and enmy.y>play1.pos[1]:
            play1.health -=20
            if play1.health ==0:
                play1.lives -=1
        enmy.y+=7

    pg.display.update()
    time.sleep(1/60)