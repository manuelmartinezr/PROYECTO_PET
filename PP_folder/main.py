
import pygame
from display import *
from sys import exit
"""""
from User import User
user = None
while user == None :
    print("b")
    user = User()

def RunningMain():
    print("a")

RunningMain()
"""""
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Posada-Plays Co')
clock = pygame.time.Clock()
font = pygame.font.Font('/Users/manuel/Documents/font/Pixeltype.ttf', 50)

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(GREEN)
text = font.render('Welcome to PyPet!', False, 'Black')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    screen.blit(text, (122, 100))
    pygame.display.update()
    clock.tick(60)
