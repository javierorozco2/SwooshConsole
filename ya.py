import pygame,sys
from pygame.locals import *
from wifi import Cell
from wireless import Wireless




pygame.init()

def wifi():

    pygame.init()
    screen=pygame.display.set_mode((480,320))
    pygame.display.set_caption("Swoosh")
    miFuentepeque = pygame.font.Font(None,60)
    fuentewifi = pygame.font.Font(None,30)
    fondo = pygame.image.load("images/ajustes/wifimenu.png")
    
    while True:
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
        #pygame.draw.rect(screen,(0,0,0),fondo2)
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit(0)
        screen.blit(fuente1,(140,100))
        screen.blit(fuente2,(140,130))
        screen.blit(fuente3,(140,160))
        screen.blit(fuente4,(140,190))
        screen.blit(fuente5,(140,220))
        screen.blit(fuente6,(140,250))
        
        
        
        
        pygame.display.update()
wifi()

