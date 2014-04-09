import sys #import des fonctions système
import os #import des fonctions os

import pygame #import de la biblioteque SDL: pygame
from pygame.locals import * #pour faciliter la lecture import des fonctions sans le pygame.*

import levelmap
import player

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

        RGBlevelmap(num_niveau)

        #creation du personnage
        self.player = Player()
        self.tous_sprites_list.add(self.player)

    def events():
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
                #if event.key == K_SPACE:
                    #if player.falling == False:
                        #player.d_vitesse_y = 0.3

    def affichage(self, fenetre):
        screen.fill(( 255, 255, 255))

        self.tous_sprites_liste.draw(fenetre)

        pygame.display.flip()


#####################
#---Boucle de jeu---#
#####################

num_niveau = '1'
game()
game = Game()
while 1:
    events()
    game.affichage(fenetre)
    fps.tick(60)

