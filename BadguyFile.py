import pygame

from Space_Shooter import *
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

class EnemyBullet(pygame.sprite.Sprite):
    '''create Enemy Bullet class'''
    def __init__(self, bullet_image, x, y):
        super().__init__()
        # scale bullet size
        self.image = pygame.transform.scale(bullet_image, (8, 23))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # bullet position is according the player position
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = 15

    def update(self):
        '''update bullet'''
        self.rect.y += self.speedy

        # if bullet goes off bottom of window, destroy it
        if self.rect.bottom > WINDOWHEIGHT:
            self.kill()
