import pygame 
import random

pygame.init()

#constants
width, height = 600, 400
cell_size = 20
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

#game window

screen = pygame.display.set_mode(600, 400)
pygame.display.set_caption("SNAKKE GAME")

