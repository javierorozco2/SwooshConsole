import pygame, sys
from moviepy.editor import VideoFileClip
from pygame.locals import *

pygame.init()

reloj = pygame.time.Clock()
x=480
y=320
fps=60

def video():
    pygame.init()
    pygame.display.set_caption("Swoosh Console")
    video = VideoFileClip("movie/Intro.mp4")
    video.preview()
    main()
def main():
    pygame.init()

    pygame.display.set_caption("Swoosh Console")
    screen = pygame.display.set_mode((x,y))
    fondo = pygame.image.load("images/Mainmenu.png")    
    
    while True:
        screen.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        pygame.display.update()
        reloj.tick(fps)
video()
