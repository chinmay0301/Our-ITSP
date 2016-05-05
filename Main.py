import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong Pong!")

#Creating 2 bars, a ball and background.
back = pygame.Surface((640,480))
background = back.convert()
background.fill((0,0,0))
bar = pygame.Surface((10,50))
goal = pygame.Surface((5,100))
bar1 = bar.convert()
bar1.fill((0,0,255))
bar2 = bar.convert()
bar2.fill((255,0,0))
goal1 = goal.convert()
goal2 = goal.convert()
goal1.fill((0,255,0))
goal2.fill((0,255,0))
circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(0,255,0),(15/2,15/2),15/2)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

# some definitions
RED = (255,0,0)
bar1_x, bar2_x = 10. , 620.
bar1_y, bar2_y = 215. , 215.
goal1_x,goal2_x = 5. , 630.
goal1_y,goal2_y = 200. , 200.
circle_x, circle_y = 307.5, 232.5
bar1_movex, bar1_movey, bar2_movey,bar2_movex = 0. , 0. , 0. , 0.
speed_x, speed_y, speed_circ = 250., 250., 250.
bar1_score, bar2_score = 0,0
#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)
hit = 0
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[K_UP]:
                bar1_movey = -ai_speed
            if keys[K_DOWN]:
                bar1_movey = ai_speed
            if keys[K_LEFT]:
                bar1_movex = -ai_speed
            if keys[K_RIGHT]:
                bar1_movex = ai_speed
            
            if keys[K_w]:
                bar2_movey = -ai_speed
            if keys[K_s]:
                bar2_movey = ai_speed
            if keys[K_a]:
                bar2_movex = -ai_speed
            if keys[K_d]:
                bar2_movex = ai_speed

        elif event.type == KEYUP:
            if event.key == K_UP:
                bar1_movey = 0.
            elif event.key == K_DOWN:
                bar1_movey = 0.
            elif event.key == K_LEFT:
                bar1_movex = 0.
            elif event.key == K_RIGHT:
                bar1_movex = 0.
            elif event.key == K_w:
                bar2_movey = 0.
            elif event.key == K_s:
                bar2_movey = 0.
            elif event.key == K_a:
                bar2_movex = 0.
            elif event.key == K_d:
                bar2_movex = 0.
 
   
    score1 = font.render(str(bar1_score), True,(255,255,255))
    score2 = font.render(str(bar2_score), True,(255,255,255))

    screen.blit(background,(0,0))
    frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
    middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
   
   
    screen.blit(bar1,(bar1_x,bar1_y))
    screen.blit(bar2,(bar2_x,bar2_y))
    screen.blit(goal1,(goal1_x,goal1_y))
    screen.blit(goal2,(goal2_x,goal2_y))
    screen.blit(circle,(circle_x,circle_y))
    screen.blit(score1,(250.,210.))
    screen.blit(score2,(380.,210.))
    bar1_y += bar1_movey
    bar1_x += bar1_movex
    bar2_y += bar2_movey
    bar2_x += bar2_movex
# movement of circle
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0

    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec
    ai_speed = speed_circ * time_sec
#AI of the computer.

    if bar1_y >= 420.: bar1_y = 420.
    elif bar1_y <= 10. : bar1_y = 10.
    if bar1_x <= 10. :bar1_x = 10.
    elif bar1_x >= 310. :bar1_x = 310.
    if bar2_y >= 420.: bar2_y = 420.
    elif bar2_y <= 10.: bar2_y = 10.
    if bar2_x >= 620. :bar2_x = 620.
    elif bar2_x <= 200. :bar2_x = 200.

    if circle_x <= bar1_x + 10 and circle_y <= bar1_y + 42.5 and circle_y >= bar1_y -7.5:
        speed_x = -speed_x
        circle_x = bar1_x + 10
    if circle_x >= bar2_x -15 and circle_y <= bar2_y + 42.5 and circle_y >= bar2_y -7.5:
        speed_x = -speed_x
        circle_x = bar2_x - 20
        hit = 1
    if circle_x < 5.: 
     if circle_y<=300 and circle_y>=200:
        bar2_score += 1
        circle_x, circle_y = 320., 232.5
        bar1_y,bar_2_y = 215., 215.
     elif not (circle_y<=300 and circle_y>=200) : speed_x = -speed_x
    elif circle_x > 620.:
      if circle_y<=300 and circle_y>=200:
        bar1_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
      elif not (circle_y<=300 and circle_y>=200): speed_x = -speed_x  
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5

    pygame.display.update()
