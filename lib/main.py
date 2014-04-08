import sys #import des fonctions système
import os #import des fonctions os

import pygame #import de la biblioteque SDL: pygame
from pygame.locals import * #pour faciliter la lecture import des fonctions sans le pygame.*

#############################
#---Fonctions principales---#
#############################

def game():
    """initialise le module pygame,
    construit la fenetre"""

    pygame.init()                                                   #initialise la biblioteque
    pygame.display.set_caption("Resets - The Revolutionary Game")   #crée le titre de la fenetre
    pygame.mouse.set_visible(0)                                     #désactive le curseur souris
    os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))         #redefini le chemin du script
    fps = pygame.time.Clock()                                       #défintion de fps (horloge du processeur)
    police = pygame.font.SysFont('Arial', 20)                       #défini la police principale

    #a mettre dans sound.py
    #son_menu = pygame.mixer.Sound('menu.wav')
    #son_menu.set_volume(.2)
    #son_niveau_1 = pygame.mixer.Sound('level_1.wav')
    #son_niveau_1.set_volume(.2)
    info_ecran = pygame.display.info()
    fenetre = pygame.display.set_mode((info_ecran.current_w, info_ecran.current_y), FULLSCREEN, 32) #affiche la fenetre en plein écran

def events():
    """teste les évenements à l'aide
     de la fonction event.get de pygame'"""
    for event in pygame.event.get():                                #parcours la liste des evenements
        if event.type == QUIT:                                      #si bouton quitter :
            pygame.quit()                                           #sortir du jeu et du script
            sys.exit()
        if event.type == KEYDOWN:                                   #si une touche est enfoncée:
            if event.key == K_ESCAPE:                               #si bouton echap :
                pygame.quit()                                       #sortir du jeu et du script
                sys.exit()
            #if event.key == K_SPACE:
                #if player.falling == False:
                    #player.d_vitesse_y = 0.3


#####################
#---Boucle de jeu---#
#####################

game()
while 1:
    events()

