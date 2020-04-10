import pygame,sys
from pygame.locals import *

reloj = pygame.time.Clock()
def juegos():

    pygame.init()
    #---------------Display---------------------
    screen = pygame.display.set_mode((480,320))
    pygame.display.set_caption("Swoosh console")
    #--------------Imagenes---------------------
    barra = pygame.image.load("images/menujuegos/barra.png")
    fondo = pygame.image.load("images/Mainmenu.png")
    #-------Variables y objetos----------------
    crono=(pygame.time.get_ticks()/1000)
    seleccion = seleccionmj(0,2)
    imagenes = presentar(0,0,crono)
    #--BUCLE--
    while True:
    	screen.blit(fondo,(0,0))
    	imagenes.update(screen)
    	#---------Evento cerrar ventana-----
    	for event in pygame.event.get():
    		if event.type == QUIT:
    			pygame.quit()
    			sys.exit(0)
    		#-----EVENTOS DE TECLADO---------
    		if event.type == pygame.KEYDOWN:
    			#---------SUBIR Y BAJAR---------
    			if event.key == K_DOWN:
    				seleccion.ax+=1
    				print seleccion.ax
    			if event.key == K_UP:
    				seleccion.ax-=1
    			#---MOVIMIENTO ENTRE OPCIONES---
    			if event.key == K_LEFT:
    				seleccion.boolatras=True
    				seleccion.boolplay=False
    			if event.key == K_RIGHT:
    				seleccion.boolplay=True
    				seleccion.boolatras=False
    			#------SELECCION DE OPCION------
    			''' CONGELADO :D
    			if event.key == K_RETURN and seleccion.boolatras==True:
    				break
    			if event.key == K_RETURN and seleccion.boolplay==True:
    				seleccion.juego()
    			'''

    	imagenes.mover(crono)
    	seleccion.acciones()
    	screen.blit(barra,(0,0))
    	seleccion.update(screen)
    	reloj.tick(60)
    	print event
    	pygame.display.update()
class seleccionmj(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		#------------------Imagenes---------------------
		self.imagen = pygame.image.load("images/menujuegos/seleccion.png")
		self.play = pygame.image.load("images/menujuegos/play.png")
		self.atras1 = pygame.image.load("images/menujuegos/atras1.png")
		self.atras2 = pygame.image.load("images/menujuegos/atras2.png")
		#-----------------Rectangulo--------------------
		self.rect = self.imagen.get_rect()
		self.rect.x = x
		self.rect.y = y
		#---------------- Variables---------------------
		self.y = y
		self.ax= 0
		self.boolplay=False
		self.boolatras=False
	def acciones(self):
		#-------------ABAJO-----------------
		if self.ax==1 and self.rect.y<=45:
			self.rect.y+=5
		if self.ax==2 and self.rect.y<=90:
			self.rect.y+=5
		if self.ax==3 and self.rect.y<=135:
			self.rect.y+=5
		if self.ax==4 and self.rect.y<=180:
			self.rect.y+=5
		if self.ax==5 and self.rect.y<=225:
			self.rect.y+=5
		if self.ax==6 and self.rect.y<=270:
			self.rect.y+=5
		if self.ax==7:
			self.ax=0
			self.rect.y=self.y
		#-----------ARRIBA-----------------
		if self.ax==5 and self.rect.y>230:
			self.rect.y-=5
		if self.ax==4 and self.rect.y>185:
			self.rect.y-=5
		if self.ax==3 and self.rect.y>140:
			self.rect.y-=5
		if self.ax==2 and self.rect.y>95:
			self.rect.y-=5
		if self.ax==1 and self.rect.y>50:
			self.rect.y-=5
		if self.ax==0 and self.rect.y>5:
			self.rect.y-=5
		if self.ax<0:
			self.ax=6
			self.rect.y=270
	def opciones(self):
		pass
	def update(self,screen):
		screen.blit(self.imagen,(self.rect.x,self.rect.y))
		screen.blit(self.atras1,(5,15))
		if self.boolatras==True:
			screen.blit(self.atras2,(5,15))
		if self.boolplay==True:
			screen.blit(self.play,(130,10))

class presentar(pygame.sprite.Sprite):
	def __init__(self,x,y,crono2):
		pygame.sprite.Sprite.__init__(self)
		self.imagen = pygame.image.load("images/capturas/panoramica.png")
		self.rect = self.imagen.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.crono2=crono2
	def mover(self,crono):
		self.crono = (pygame.time.get_ticks()/1000)-self.crono2
		if self.crono>=3 and self.rect.x>(-480):
			self.rect.x-=5
		if self.crono>=8 and self.rect.x>(-960):
			self.rect.x-=5

		if self.crono == 13:
			self.crono2+=13
			self.rect.x=0


	def update(self,screen):
		screen.blit(self.imagen,(self.rect.x,self.rect.y))


juegos()

