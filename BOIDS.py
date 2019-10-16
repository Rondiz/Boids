#!/usr/bin/env python

import random
import pygame
import math
from sys import exit

pygame.init()
height = 400
width = height
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BOIDS")
white = (255, 255, 255)
black = (0, 0, 0)
bvelocity = 5
bdim = 5
colldist = 50

clock = pygame.time.Clock()

class Boid:
    
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.pos = (self.x, self.y)
        self.dx = random.random()
        self.dy = random.random()
        self.dirv = (self.dx, self.dy)

    def draw(self):
        pygame.draw.circle(screen, white, self.pos, bdim)

    def detect_wall_collision(self):
        tx = int(self.x+self.dx*colldist)
        ty = int(self.y+self.dy*colldist)
        ##pygame.draw.line(screen, white, self.pos, (tx, ty))
        
        if (ty < 0 or ty > width):
            if (ty < 0):
                ty = -ty
            else:
                ty = width - (ty - width) 
            angle = math.atan2(ty-self.y, tx-self.x)
            self.dx = math.cos(angle)
            self.dy = math.sin(angle)

        if (tx < 0 or tx > height):
            if (tx < 0):
                tx = -tx
            else:
                tx = height - (tx - height) 
            angle = math.atan2(tx-self.x, ty-self.y)
            self.dx = math.sin(angle)
            self.dy = math.cos(angle)

    def move(self):
        self.detect_wall_collision()
        self.x += int(self.dx*bvelocity)
        self.y += int(self.dy*bvelocity)
        self.pos = (self.x, self.y)
        

b = Boid()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(black)
    b.move()
    b.draw()
    
    pygame.display.flip()
    clock.tick(60)
