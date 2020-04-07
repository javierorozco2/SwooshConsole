import pygame,sys
from pygame.locals import *

pygame.init()
reloj = pygame.time.Clock()
fps=30
sonidofondo = pygame.mixer.music.load("movie/Intro.ogg")
pygame.mixer.music.play(100)

def main():

        pygame.init()
        pygame.display.set_caption("Swoosh Console")
        screen = pygame.display.set_mode((480,320))
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
                break