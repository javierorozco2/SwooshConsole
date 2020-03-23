import pygame, sys
from moviepy.editor import VideoFileClip
from pygame.locals import *

pygame.init()

reloj = pygame.time.Clock()
x=480
y=320
fps=60


def musica():
    pygame.mixer.music.load("MusicaAmbiente1.mp3")
    pygame.mixer.music.play(1)

def video():
    pygame.init()
    pygame.display.set_caption("Swoosh Console")
    video = VideoFileClip("Animacion.mp4")
    video.preview()
    main()
def main():
    pygame.init()

    pygame.display.set_caption("Swoosh Console")
    screen = pygame.display.set_mode((x,y))

    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        pygame.display.update()
        reloj.tick(fps)
musica()
video()
