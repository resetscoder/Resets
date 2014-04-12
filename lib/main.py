import sys #import des fonctions système
import os #import des fonctions os

import pygame #import de la biblioteque SDL: pygame
from pygame.locals import * #pour faciliter la lecture import des fonctions sans le pygame.*

import levelmap
from player import *

#############################
#---Fonctions principales---#
#############################

def game():
    global fenetre, LARGEUR, HAUTEUR, fps
    """initialise le module pygame,
    construit la fenetre"""

    pygame.init()                                                   #initialise la biblioteque
    pygame.display.set_caption("Resets - The Revolutionary Game")   #crée le titre de la fenetre
    pygame.mouse.set_visible(0)                                     #désactive le curseur souris
    DOSSIER_COURRANT = os.path.dirname(sys.argv[0])         #redefini le chemin du script
    DOSSIER_PARENT = os.path.dirname(DOSSIER_COURRANT)
    sys.path.append(os.path.join(DOSSIER_PARENT, 'data'))
    fps = pygame.time.Clock()                                       #défintion de fps (horloge du processeur)
    police = pygame.font.SysFont('Arial', 20)                       #défini la police principale

    #a mettre dans sound.py
    #son_menu = pygame.mixer.Sound('menu.wav')
    #son_menu.set_volume(.2)
    #son_niveau_1 = pygame.mixer.Sound('level_1.wav')
    #son_niveau_1.set_volume(.2)
    info_ecran = pygame.display.Info()
    LARGEUR = info_ecran.current_w
    HAUTEUR = info_ecran.current_h
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), FULLSCREEN, 32) #affiche la fenetre en plein écran

class Game():

     # Listes des sprites
    bloc_liste = None
    tous_sprites_liste = None
    player = None

    def __init__(self):

        #création des listes de sprites
        self.bloc_liste = pygame.sprite.Group()
        self.tous_sprites_liste = pygame.sprite.Group()

        #ajout des sprites

        niveau = levelmap.RGBlevelmap()
        niveau.bloc_level(1360,766,self.bloc_liste,self.tous_sprites_liste)

        #creation du personnage
        self.player = Player()
        self.tous_sprites_liste.add(self.player)

    def events(self,game):
        """teste les évenements à l'aide
        de la fonction event.get de pygame"""
        for event in pygame.event.get():                                #parcours la liste des evenements
            if event.type == QUIT:                                      #si bouton quitter :
                pygame.quit()                                           #sortir du jeu et du script
                sys.exit()
            if event.type == KEYDOWN:                                   #si une touche est enfoncée:
                if event.key == K_ESCAPE:                               #si bouton echap :
                    pygame.quit()                                       #sortir du jeu et du script
                    sys.exit()
                """if event.key == K_SPACE:
                    if player.falling == False:
                        if vitesse_x == 0:
                            game.player.saut()
                        else:
                            game.player.gravitenewton()
                if event.key == K_q:
                    player.aller_gauche += 6
                if event.key == K_d:
                    player.aller_droite += 6
                if event.key == K_q and event.key == K_LSHIFT:
                    player.aller_gauche += 9
                if event.key == K_d and event.key == K_LSHIFT:
                    player.aller_droite += 9"""

    def affichage(self, fenetre):
        fenetre.fill(( 0, 0, 0))

        self.tous_sprites_liste.draw(fenetre)

        pygame.display.flip()


#####################
#---Boucle de jeu---#
#####################

num_niveau = '1'
game()
jeu = Game()
while 1:
    jeu.events(game)
    jeu.affichage(fenetre)
    fps.tick(60)

