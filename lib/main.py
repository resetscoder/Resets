import sys
import os

import pygame
from pygame.locals import *

def game():
    """initialise le module pygame,
    construit la fenetre"""

    pygame.init()
    pygame.display.set_caption("Resets - The Revolutionary Game")
    os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
    fps = pygame.time.Clock()
    police = pygame.font.SysFont('Arial', 20)

    #a mettre dans sound.py
    #son_menu = pygame.mixer.Sound('menu.wav')
    #son_menu.set_volume(.2)
    #son_niveau_1 = pygame.mixer.Sound('level_1.wav')
    #son_niveau_1.set_volume(.2)

    fenetre = pygame.display.set_mode((450, 300), 0, 32)