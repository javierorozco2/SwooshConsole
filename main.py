import pygame, sys
from moviepy.editor import VideoFileClip
from pygame.locals import *

pygame.init()

reloj = pygame.time.Clock()
x=480
y=320
fps=60
#-------------------FUNCIONES--------------------
def video():
    pygame.init()
    pygame.display.set_caption("Swoosh Console")
    video = VideoFileClip("movie/Intro.mp4")
    video.preview()
    main()
def main():
    pygame.init()

    #-----------------SCREEN----------------
    pygame.display.set_caption("Swoosh Console")
    screen = pygame.display.set_mode((x,y))
    #----------------IMAGENES---------------
    fondo = pygame.image.load("images/Mainmenu.png")
    botonjuegos1 = pygame.image.load("images/botonjuegos.png")
    botonjuegos2 = pygame.image.load("images/botonjuegos2.png")
    botonajuste1 = pygame.image.load("images/botonajustes.png")
    botonajuste2 = pygame.image.load("images/botonajustes2.png")
    botoninternet1 = pygame.image.load("images/botoninternet.png")
    botoninternet2 = pygame.image.load("images/botoninternet2.png")
    botonsalir1 = pygame.image.load("images/botonsalir.png")
    botonsalir2 = pygame.image.load("images/botonsalir2.png")
    #------------CLASES Y VARIABLES---------
    cursor1 = cursor()    
    botonjuegos = Boton(botonjuegos1,botonjuegos2,0,190)
    botonajustes = Boton(botonajuste1,botonajuste2,0,250)
    botoninternet = Boton(botoninternet1,botoninternet2,287,190)
    botonsalir = Boton(botonsalir1,botonsalir2,292,250)
    while True:
        screen.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        cursor1.update()
        botonjuegos.update(screen,cursor1)
        botonajustes.update(screen,cursor1)
	botoninternet.update(screen,cursor1)
        botonsalir.update(screen,cursor1)
        pygame.display.update()
        reloj.tick(fps)
#-----------AQUI VAN TODAS LAS CLASES-------------------
class cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,botonjugar,botonjugar2,x,y):
        self.imagen_normal=botonjugar
        self.imagen_seleccion=botonjugar2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self,screen,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal

        screen.blit(self.imagen_actual,self.rect)

#-----------LLAMADO DE CLASE PRINCIPAL-----------
#main()
video()
