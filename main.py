import pygame, sys, os
from pygame.locals import *
from Tkinter import *
from wifi import Cell
from wireless import Wireless
from pygame_vkeyboard import *


pygame.init()

reloj = pygame.time.Clock()
x=480
y=320
fps=300
miFuentepeque = pygame.font.Font(None,33)

#-------------------FUNCIONES--------------------
def video():
        pygame.init()
        pygame.display.set_caption("Swoosh Console")
        
        screen = pygame.display.set_mode((480,320))
        screen = pygame.display.set_mode((480,320))

        sonidofondo = pygame.mixer.music.load("movie/Intro.ogg")
        pygame.mixer.music.play(1)
        valor=1
        while True:
            if (valor<10):
                palabra="movie/frames/scene0000"
                palabra+=str(valor)
                palabra+=".png"
            if (valor<100 and valor>9):
                palabra="movie/frames/scene000"
                palabra+=str(valor)
                palabra+=".png"
            if (valor<100 and valor>9):
                palabra="movie/frames/scene000"
                palabra+=str(valor)
                palabra+=".png"
            if (valor<536 and valor>99):
                palabra="movie/frames/scene00"
                palabra+=str(valor)
                palabra+=".png"
            screen.blit(pygame.image.load(palabra),(0,0))
            valor+=1
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()
            reloj.tick(fps)
            if valor==535:
                pygame.mixer.music.stop()
                pygame.mixer.music.stop()

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
                    os.system("chromium-browser %U")
                    #teclado os.system("") 
                     
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
    flecha = pygame.image.load("images/ajustes/flecha1.png")
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
                #-------------MOVIMIENTOS DEL CUADRO SELECCION----------
                if event.key == pygame.K_DOWN and seleccion1.pFlecha==False:
                    seleccion1.ax+=1
                if event.key == pygame.K_UP and seleccion1.pFlecha==False:
                    seleccion1.ax-=1
                #-----------------------SELECCIONAR----------------------
                if event.key == pygame.K_RETURN:
                    seleccion1.opcion()
                #------------------MOVIMIENTO DEL VOLUMEN----------------
                if event.key == pygame.K_RIGHT and seleccion1.ax==0:
                    if tam<100:
                        tam+=10
                        #Falta agregar modificacion de volumen
                if event.key == pygame.K_LEFT and seleccion1.ax==0:
                    if tam>0:
                        tam-=10
                        #Falta agregar modificacion de volumen
                #--------------------POSICION SALIR---------------------
                if event.key == pygame.K_RIGHT:
                    seleccion1.pFlecha=False
                if event.key == pygame.K_LEFT and seleccion1.ax!=0:
                    seleccion1.pFlecha=True
        #---------CARGA DE IMAGENES Y OBJETOS-------------
        screen.blit(flecha,(10,150))
        screen.blit(porcentajevol,(395,97))
        pygame.draw.rect(screen,(67,75,77),rfondo)
        pygame.draw.rect(screen,(255,255,255),r1)
        seleccion1.acciones()
        seleccion1.update(screen)
        cursor1.update()
        pygame.display.update()
        reloj.tick(fps)

def wifi():

    pygame.init()
    #---------------DISPLAY------------------
    screen=pygame.display.set_mode((480,320))
    pygame.display.set_caption("Swoosh")
    #--------------IMAGENES------------------
    atras=pygame.image.load("images/ajustes/flecha1.png")
    fondo = pygame.image.load("images/ajustes/wifimenu.png")
    #----------VARIABLES Y METODOS-----------
    miFuentepeque = pygame.font.Font(None,60)
    fuentewifi = pygame.font.Font(None,30)
    seleccion = selecwifi(69,96)
    ciclo = True
    #--BUCLE---
    while ciclo==True:
        a = {}
        i = 0
        for i in range(0,6):
            a[i]="--------------"
        c = 0
        for cell in Cell.all('wlan0'):
            a[c] = cell.ssid
            c += 1
        
        fuente1 = fuentewifi.render(str(a[0]),0,(255,255,255))
        fuente2 = fuentewifi.render(str(a[1]),0,(255,255,255))
        fuente3 = fuentewifi.render(str(a[2]),0,(255,255,255))
        fuente4 = fuentewifi.render(str(a[3]),0,(255,255,255))
        fuente5 = fuentewifi.render(str(a[4]),0,(255,255,255))
        fuente6 = fuentewifi.render(str(a[5]),0,(255,255,255))    
        screen.blit(fondo,(0,0))
        #-------REGISTRO DE EVENTOS-----
        for event in pygame.event.get():
            
            if event.type==QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                #-------ABAJO Y ARRIBA-------
                if event.key == pygame.K_DOWN and seleccion.boolatras==False:
                    seleccion.ax+=1
                if event.key == pygame.K_UP and seleccion.boolatras==False:
                    seleccion.ax-=1
                #------ATRAS O NO ATRAS------
                if event.key == pygame.K_RIGHT:
                    seleccion.boolatras=False
                if event.key == pygame.K_LEFT:
                    seleccion.boolatras=True
                #---------SALIR Y SELECCIONAR---------
                if event.key == pygame.K_RETURN and seleccion.boolatras==True:
                    ciclo = False
                if event.key == pygame.K_RETURN and seleccion.boolatras==False:
                    ssid = str(a[seleccion.ax]) 
                    wififinal(ssid)
                
        screen.blit(fuente1,(140,100))
        screen.blit(fuente2,(140,130))
        screen.blit(fuente3,(140,160))
        screen.blit(fuente4,(140,190))
        screen.blit(fuente5,(140,220))
        screen.blit(fuente6,(140,250))
        screen.blit(atras,(10,150))
        seleccion.acciones()
        seleccion.update(screen)
        pygame.display.update()

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
        self.flecha2 = pygame.image.load("images/ajustes/flecha2.png")
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.introja=0
        self.introjaw=0
        self.control = y
        self.ax=0
        self.pFlecha=True

    def acciones(self):
        if self.pFlecha==False:
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
        if self.pFlecha==False:

            #Opcion actualizar
            if self.ax==3:
                os.system("git pull")
                pygame.quit()
                os.system("python main.py")
         
            #Opcion wifi
            if self.ax==2:
                wifi()

            #Opcion sonido
            if self.ax==1:
                self.introja+=1
        else:
            main()
        #Activacion de linea roja
        if self.introja>1 or self.introjaw>1:
            self.introja=0
            self.introjaw=0
                        

    def update(self,screen):
        if self.pFlecha==True:
            screen.blit(self.flecha2,(10,150))
        else:
            screen.blit(self.imagen,(self.rect.x,self.rect.y))
            if self.introja==1:
                screen.blit(self.roja,(390,135))      
            if self.introjaw==1:
                screen.blit(self.roja,(390,178))  

class selecwifi(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load("images/ajustes/seleccionwifi.png")
        self.atras = pygame.image.load("images/ajustes/flecha2.png")
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.control = y
        self.ax=0
        self.boolatras = True
    def acciones(self):
        if self.boolatras==False:
            #----------ABAJO------------------
            if self.ax==1 and self.rect.y<=125:
                self.rect.y+=2
            if self.ax==2 and self.rect.y<=154:
                self.rect.y+=2
            if self.ax==3 and self.rect.y<=185:
                self.rect.y+=2
            if self.ax==4 and self.rect.y<=214:
                self.rect.y+=2
            if self.ax==5 and self.rect.y<=244:
                self.rect.y+=2
            if self.ax==6:
                self.ax=0
                self.rect.y=self.control
            #---------ARRIBA-------------------
            if self.ax==4 and self.rect.y>216:
                self.rect.y-=2
            if self.ax==3 and self.rect.y>186:
                self.rect.y-=2
            if self.ax==2 and self.rect.y>156:
                self.rect.y-=2
            if self.ax==1 and self.rect.y>126:
                self.rect.y-=2
            if self.ax==0 and self.rect.y>96:
                self.rect.y-=2
            if self.ax<0:
                self.ax=5
                self.rect.y=244
    def update(self,screen):
        if self.boolatras==True:
            screen.blit(self.atras,(10,150))
        else:
            screen.blit(self.imagen,(self.rect.x,self.rect.y))
    
#///////////////////////////////////////////////////////////////////////////////    
            
def wififinal(ssid):
    pygame.init()
    #---------------DISPLAY------------------
    window=pygame.display.set_mode((480,320))
    pygame.display.set_caption("Swoosh")
    
    #--------------IMAGENES------------------
    fondo = pygame.image.load("images/ajustes/wifipass.png")

    #------------.VARIABLES------------------------
    fuentewifi = pygame.font.Font(None,30)
    fuentessid = fuentewifi.render(ssid,0,(255,255,255))
    
    def consumer(text):
        print(repr('Current text state: %s' % text))
        fuente1 = fuentewifi.render(str(text),0,(255,255,255))
        window.blit(fuente1,(140,60))

    while True:
        window.blit(fondo,(0,0)) #fondo de teclado
        layout = VKeyboardLayout(VKeyboardLayout.AZERTY) #tipo de teclado
        keyboard = VKeyboard(window, consumer, layout) #teclado
        keyboard.enable() #teclado activado
        running = True
        while running:
            window.blit(fuentessid,(200,15))
            pygame.display.flip()
            pygame.display.update()
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                keyboard.on_event(event)
                
            #pygame.display.update()
        
#///////////////////////////////////////////////////////////////////////////////       
    
    
    
    

#-----------LLAMADO DE CLASE PRINCIPAL-----------
main()
#video()
