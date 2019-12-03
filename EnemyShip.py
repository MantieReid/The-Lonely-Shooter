import random
import pygame, random
from pygame import *
from os import path

from EnemyShip import *

img_dir = path.join(path.dirname(__file__), 'images')
sound_dir = path.join(path.dirname(__file__), 'sounds')

WINDOWWIDTH = 480
WINDOWHEIGHT = 600
FPS = 30

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREENYELLOW = (143,245,34)
YELLOW = (234, 245, 34)
GREY = (210,210,210)
DARKGREY = (93,94,94)
RED = (255,0,0)
GREEN = (0,255,0)
REDORANGE = (245,103,32)

# initialize pygame and create window
pygame.init()
pygame.mixer.init() # initialize for sound
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('The Lonely Shooter')

FPSCLOCK = pygame.time.Clock() # For syncing the FPS

import pygame

from Space_Shooter import WINDOWWIDTH, WINDOWHEIGHT, Boost
from BadguyFile import EnemyBullet


class EnemyShip(pygame.sprite.Sprite):
    '''create EnemyShip class'''
    def __init__(self, enemy_image, bullet_image, sprites_list, bullet_list, bullet_sound, boost_anim):
        super().__init__()
        # scale enemy image
        self.image = pygame.transform.scale(enemy_image, (60, 60))
        self.rect = self.image.get_rect()

        # sprites list
        self.sprites = sprites_list
        self.boost_anim = boost_anim

        # enemy starting location
        self.rect.centerx = random.randrange(90, WINDOWWIDTH - 90)
        self.rect.bottom = random.randrange(-150, -20)

        # bullet attributes for enemy
        self.bullet_image = bullet_image
        self.bullet_sound = bullet_sound
        self.bullets = bullet_list
        self.shoot_delay = 500
        self.last_shot = pygame.time.get_ticks()
        self.num_of_shots = 2

        # enemy kamikaze boost speed
        self.speedy = 30

    def update(self):
        '''update enemy movement'''
        if self.rect.bottom > 50 and self.rect.bottom < 130:
            for i in range(self.num_of_shots):
                    self.shoot()

        if self.rect.bottom <= 120:
            self.rect.bottom += 4
        if self.rect.bottom > 120 and self.rect.bottom < 140:
            self.rect.bottom += 1
        if self.rect.bottom >= 140:
            self.divebomb()

        # if ships go off the screen, respawn them
        if (self.rect.top > WINDOWHEIGHT):
            self.rect.centerx = random.randrange(50, WINDOWWIDTH - 50)
            self.rect.y = random.randrange(-200, -50)

    def shoot(self):
        '''fire lasers'''
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_delay:
            self.last_shot = current_time
            bullet = EnemyBullet(self.bullet_image, self.rect.centerx, self.rect.bottom)
            self.sprites.add(bullet)
            self.bullets.add(bullet)
            self.bullet_sound.play()
            self.bullet_sound.set_volume(0.2)

    def divebomb(self):
        '''divebomb flight pattern'''
        boost = Boost(self.rect.center, 'boost', self.boost_anim)
        self.sprites.add(boost)
        self.rect.bottom += self.speedy
