#Import 2 libraries to our game
import pygame
import random

#Initialise the pygame
pygame.init()

#Declare some variables/constants
winHeight = 480
winWidth = 700
Purple = (255, 0,255)

#Create window game
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hangman by Luke")

#Main Program
#Create a game Loop to keep the game visible
inPlay = True
while inPlay:
    win.fill(Purple) #Makes Backgroud colour Green
    pygame.display.update()
    pygame.time.delay(100)

#Quit The Program
pygame.quit()
