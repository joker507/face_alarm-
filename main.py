# coding=UTF-8
import facedelication
import pygame

import time
def main():
    pygame.mixer.init()
    music = pygame.mixer.music
    music.load ( "newfile.wav")
    music.play(-1)
    facedelication.facealarm()
    music.stop()
    pygame.mixer.init(frequency=15500,size=-16,channels=4)
    music.load("result.wav")
    music.play(1)
    while(music.get_busy()==1):
        time.sleep(0.1)
if(__name__=='__main__'):
    main()