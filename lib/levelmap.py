import pygame
from pygame.locals import *

import sprites 
import tiles
import main

def RGBlevelmap(num_niveau):
    #penser à l'arrière plan !
    del plateformes[:], ennemis[:]
    img_niveau = pygame.image.load('Level_%s.png'%(num_niveau)).convert_alpha()
    for x in range(img_niveau.get_width()):
        for y in range(img_niveau.get_height()):
            color = img_niveau.get_at((x,y))
            x = x*(largeur/img_niveau.get_width())
            y = y*(hauteur/img_niveau.get_heigh())
            if color == (,,,):
                Plateform('0_level%s.png'%(num_niveau),x,y)
            if color == (,,,):
                Plateform('1_level%s.png'%(num_niveau),x,y)
            #etc...
