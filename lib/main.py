import sys #import des fonctions système
import os #import des fonctions os

import pygame #import de la biblioteque SDL: pygame
from pygame.locals import * #pour faciliter la lecture import des fonctions sans le pygame.*

from constantes import *
import game

#############################
#---Fonctions principales---#
#############################

def initialisation():
    global fenetre, fps
    """initialise le module pygame,
    construit la fenetre"""

    pygame.display.set_caption("Resets - The Revolutionary Game")   #crée le titre de la fenetre
    pygame.mouse.set_visible(0)                                     #désactive le curseur souris
    
    fps = pygame.time.Clock()                                       #définition de fps (horloge du processeur)
    police = pygame.font.SysFont('Arial', 20)                       #défini la police principale

    #a mettre dans sound.py
    #son_menu = pygame.mixer.Sound('menu.wav')
    #son_menu.set_volume(.2)
    #son_niveau_1 = pygame.mixer.Sound('level_1.wav')
    #son_niveau_1.set_volume(.2)

    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), FULLSCREEN, 32) #affiche la fenetre en plein écran

#####################
#---Boucle de jeu---#
#####################

num_niveau = '1' #provisoire
level = False
initialisation()
jeu = game.Game(num_niveau,level)
while 1:
    jeu.events()
    jeu.affichage(fenetre)
    fps.tick(60)

