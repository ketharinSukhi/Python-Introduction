import pygame 
import random

pygame.init()

#constants
width, height = 600, 400
cell_size = 30
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

#game window

screen = pygame.display.set_mode(width, height)
pygame.display.set_caption("SNAKKE GAME")

#snake initialization
snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (cell_size, 0)

