#Make Prettier

import pygame
import random

pygame.init()

black = (0,0,0)
white = (255,255,255)
skyBlue = (0,191,255)
green = (0,255,0)
red = (255,0,0)

size = (400,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy Bird")

done = False
clock = pygame.time.Clock()

x = 200
y = 250
x_speed = 0
y_speed = 0
ground = 477
xloc=400
yloc = 0
xsize = 70
ysize = random.randint(0,350)
space = 150
obspeed = 2.5
score = 0

highScore = 0

def obstacles(xloc,yloc,xsize,ysize):
    
    
    pygame.draw.rect(screen,black,  [xloc-3, yloc, xsize+6, ysize+3])
    pygame.draw.rect(screen,black, [xloc-3, int(yloc+ysize+space)-3,xsize+6,ysize+497])
    pygame.draw.rect(screen,green, [xloc,yloc,xsize,ysize])
    pygame.draw.rect(screen,green, [xloc,int(yloc+ysize+space), xsize, ysize+500])

imageUp = pygame.image.load('flappy_up.png')
imageDown = pygame.image.load('flappy_down.png')
imageUp = pygame.transform.scale(imageUp, (40,40))
imageDown = pygame.transform.scale(imageDown, (80,40))

def flappy(x,y, y_speed):
    if y_speed < 0:
        #falling image
        screen.blit(imageUp, (x,y))
    elif y_speed >= 0:
        #flapping image
        screen.blit(imageDown, (x-20,y-10))

def gameover():
    font = pygame.font.SysFont(None,50)
    text = font.render("Game Over ",True,red)
    screen.blit(text, [200,250])

#function to write score being kept
def Score(score):
    font = pygame.font.SysFont(None,70)
    text = font.render(str(score),True,white)
    screen.blit(text, [200,62])
    
def high_score(highScore):
    font = pygame.font.SysFont(None,30)
    text = font.render("High Score: "+str(highScore),True,black)
    screen.blit(text, [250,0])
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -10 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = 200
                y = 250
                x_speed = 0
                y_speed = 0
                ground = 477
                xloc=400
                yloc = 0
                xsize = 70
                ysize = random.randint(0,350)
                space = 150
                obspeed = 2.5
                score = 0
        
    screen.fill(skyBlue)    
    obstacles(xloc,yloc,xsize,ysize)
    flappy(x,y,y_speed)    
    #if the ball is between to obstacles 
    Score(score)
    high_score(highScore)
    
    y += y_speed
    xloc -= obspeed
    if score >= highScore:
        highScore = score
    elif score < highScore:
        highScore
    if y > ground:
        gameover()
        y_speed = 0
        obspeed = 0
    
    #if we hit obstacles in the top block
    if x+40 > xloc and y < ysize and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 0
        
    #if we hit obstacles in the bottom block
    if x+20 > xloc and y+25 > ysize+space and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 0
    
    #if obstacle location X is 
    if xloc < -80:
        xloc = 400
        ysize = random.randint(0,350)
    
    #check if obstacle was passed adding to score
    if x > xloc and x < xloc+3:
        score = (score + 1)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
    
print "High Score: " + str(highScore)