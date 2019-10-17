#!/bin/py

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
            angle = math.degrees(math.atan2(ty-self.y, tx-self.x))
            print(f"Angle ty: {angle}")
            self.dx = math.cos(angle)
            if(angle == 90):
                self.dx += 0.1
            self.dy = math.sin(angle)

        if (tx < 0 or tx > height):
            if (tx < 0):
                tx = -tx
            else:
                tx = height - (tx - height) 
            angle = math.degrees(math.atan2(tx-self.x, ty-self.y))
            print(f"Angle tx: {angle}")
            self.dx = math.sin(angle)
            self.dy = math.cos(angle)
            if(angle == 90):
                self.dy += 0.1

    def move(self):
        self.detect_wall_collision()
        if(self.dx == 0):
            self.x += 0
        else:
            local_x_velocity = bvelocity/self.dx
            print(f"x vel:  {local_x_velocity}")
            print(f"total: {local_x_velocity*self.dx}")
            self.x += int(self.dx*(self.dx*local_x_velocity))
        if(self.dy == 0):
            self.y += 0
        else:
             local_y_velocity = bvelocity/self.dy
             print(f"y vel:  {local_y_velocity}")
             print(f"total: {local_y_velocity*self.dy}")
             self.y += int(self.dy*(self.dy*local_y_velocity))
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
