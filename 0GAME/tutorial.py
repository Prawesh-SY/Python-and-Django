import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Mission Titan")         # Displays the caption of the console window

WIDTH, HEIGHT = 1000, 770                           # The height and width of the console window is determined
FPS = 60                                            # The refresh rate of the console window is determined
PLAYER_VEL = 3                                      # The speed of the spaceship is determined

window = pygame.display.set_mode((WIDTH,HEIGHT))    # The object of the display is created


class SpaceShuttle(pygame.sprite.Sprite):
    COLOR = (255,0 ,0)
    GRAVITY = 1
    
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animationCount = 0
        self.fall_count = 0
        self.thruster_count = 0
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # self.rect.
    def moveLeft(self, vel):
        self.x_vel += -vel
        if self.direction != "left":
            self.direction = 'left'
            self.animationCount = 0
        
    def moveRight(self, vel):
        self.x_vel += vel
        if self.direction != "right":
            self.direction = 'right'
            self.animationCount = 0
    
    def moveUp(self, vel):
        self.y_vel += -vel
        pass
    
    def moveDown(self, vel):
        self.y_vel += vel
    
             
    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count/fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)
        
        self.fall_count += 1
        
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)

class Stages(SpaceShuttle):
    GRAVITY = 1
    
    def __init__(self):
        pass
    
    def stage_1(self,fall_count, fps):
        stage_1_Gravity = 0
        stage_1_Gravity += min(1, (fall_count / fps) * self.GRAVITY)
        return stage_1_Gravity
        pass


def getBackground(name):
    image = pygame.image.load(join("assets","Background", name))
    _,_,width,height = image.get_rect()
    tiles = []
    
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image

def draw(window, background, bgImage, spaceShip):
    for tile in background:
        window.blit(bgImage, tile)
    
    spaceShip.draw(window)
        
    pygame.display.update()

def handle_move(spaceShip):
    keys = pygame.key.get_pressed()
    
    # spaceShip.y_vel = 0
    spaceShip.x_vel = 0
    if keys[pygame.K_LEFT]:
        spaceShip.moveLeft(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        spaceShip.moveRight(PLAYER_VEL)
    if keys[pygame.K_UP]:
        spaceShip.moveUp(PLAYER_VEL)
    if keys[pygame.K_DOWN]:
        spaceShip.moveDown(PLAYER_VEL)
def main(window):
    clock = pygame.time.Clock()
    background, bgImage = getBackground("Space.png")
    
    spaceShip = SpaceShuttle(100, 100, 50, 50)
    
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 
        
        spaceShip.loop(FPS)
        handle_move(spaceShip)
        draw(window,background, bgImage, spaceShip)
    
    pygame.quit()
    quit()
    
    
if __name__ == "__main__":
    main(window)