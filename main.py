import pygame, sys, os
from pygame.locals import *

pygame.init()

reloj = pygame.time.Clock()
x=480
y=320
fps=60
miFuentepeque = pygame.font.Font(None,33)
#-------------------FUNCIONES--------------------
def video():
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(botonsalir.rect):
                    pygame.quit()
                if cursor1.colliderect(botoninternet.rect):
                    os.system("google-chrome")
                if cursor1.colliderect(botonajustes.rect):
                    ajustes()
        cursor1.update()
        botonjuegos.update(screen,cursor1)
        botonajustes.update(screen,cursor1)
        botoninternet.update(screen,cursor1)
        botonsalir.update(screen,cursor1)
        pygame.display.update()
        reloj.tick(fps)

def ajustes():
    pygame.init()

    #-----------------SCREEN----------------
    pygame.display.set_caption("Swoosh Console")
    screen = pygame.display.set_mode((x,y))
    #----------------IMAGENES---------------
    fondo = pygame.image.load("images/ajustes/ajustes.png")
    #------------CLASES Y VARIABLES---------
    cursor1 = cursor()
    seleccion1 = seleccion(40,85)
    rfondo = pygame.Rect(280,100,100,15)
    tam=100
    #-----------BUCLE DE AJUSTES------------
    while True:
        r1 = pygame.Rect(280,100,tam,15)
        porcentajevol = miFuentepeque.render(str(tam),0,(255,255,255))
        screen.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    seleccion1.ax+=1
                if event.key == pygame.K_UP:
                    seleccion1.ax-=1
                if event.key == pygame.K_RETURN:
                    seleccion1.opcion()
                if event.key == pygame.K_RIGHT and seleccion1.ax==0:
                    if tam<100:
                        tam+=10
                        #Falta agregar modificacion de volumen
                if event.key == pygame.K_LEFT and seleccion1.ax==0:
                    if tam>0:
                        tam-=10
                        #Falta agregar modificacion de volumen
        screen.blit(porcentajevol,(395,97))
        pygame.draw.rect(screen,(67,75,77),rfondo)
        pygame.draw.rect(screen,(255,255,255),r1)
        seleccion1.acciones()
        seleccion1.update(screen)
        cursor1.update()
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

class seleccion(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load("images/ajustes/ajustesSelec.png")
        self.roja = pygame.image.load("images/ajustes/ajustesLroja.png")
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.introja=0
        self.introjaw=0
        self.control = y
        self.ax=0

    def acciones(self):
        #-------Movimiento K_DOWN(abajo)--------
        if (self.ax==1 and self.rect.y<=120):
            self.rect.y+=5
        if (self.ax==2 and self.rect.y<=170):
            self.rect.y+=5
        if (self.ax==3 and self.rect.y<=205):
            self.rect.y+=5
        if self.ax==4:
            self.ax=0
            self.rect.y= self.control
        #-------Movimiento K_UP(arriba)--------
        if (self.ax==2 and self.rect.y >170):
            self.rect.y-=5
        if (self.ax==1 and self.rect.y >125):
            self.rect.y-=5
        if (self.ax==0 and self.rect.y >self.control):
            self.rect.y-=5
        if (self.ax==-1):
            self.ax=3
            self.rect.y=205
    def opcion(self):
        #Opcion actualizar
        if self.ax==3:
            os.system("git pull")
            pygame.quit()
            os.system("python main.py")
        #Opcion wifi
        if self.ax==2:
            self.introjaw+=1
        #if self.introjaw==0:
            #os.system("sudo ifconfig wlo1 up")
        #else:
            #os.system("sudo ifconfig wlo1 down")
        #Opcion sonido
        if self.ax==1:
            self.introja+=1

        if self.introja>1 or self.introjaw>1:
            self.introja=0
            self.introjaw=0
                        

    def update(self,screen):
        screen.blit(self.imagen,(self.rect.x,self.rect.y))
        if self.introja==1:
            screen.blit(self.roja,(390,135))      
        if self.introjaw==1:
            screen.blit(self.roja,(390,178))  

#-----------LLAMADO DE CLASE PRINCIPAL-----------
#main()
video()
