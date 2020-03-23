import pygame
from pygame.locals import *
import sys

# -----------
# Constantes
# -----------

FPS = 60
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320


# ------------------------------
# Funcion principal del juego
# ------------------------------

def main():
    pygame.init()
    # VENTANA Y TITULO:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Swoosh Game")
    background = pygame.Surface((480, 320))
    #RELOG
    reloj = pygame.time.Clock()


    #IMAGENES A SURFACE
    #fondo1 = pygame.image.load("Intro1.png").convert()

    #POSICION DE LOS SURFACES (IMAGENES)
    #screen.blit(fondo1, (0, 0)) 
    
    #MOSTRAR IMAGENES EN PANTALLA 
    #pygame.display.flip()


    #VIDEO
    movie = pygame.movie.Movie('Animacion.mpg')
    screen = pygame.display.set_mode(movie.get_size())
    movie_screen = pygame.Surface(movie.get_size()).convert()  #NO FUNCIONA 
    movie.set_display(movie_screen)
    movie.play()
     


    #MUSICA
    pygame.mixer.music.load("MusicaAmbiente1.mp3")
    pygame.mixer.music.play(1)

    # BUCLE PRINCIPAL DEL JUEGO
    while True:
        # ENTRADAS BOTONES O TECLAS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
