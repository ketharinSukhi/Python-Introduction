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

#food initialization
food = (random.randint(0, (width // cell_size)-1) * cell_size,
        random.randint(0, (height // cell_size)-1) * cell_size)

clock = pygame.time.Clock()
score = 0
running = True

while running:
    screen.fill(black)

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, cell_size):
                snake_dir = (0, -cell_size)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -cell_size):
                snake_dir = (0, cell_size)
            elif event.key == pygame.K_LEFT and snake_dir != (cell_size, 0):
                snake_dir = (-cell_size, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-cell_size, 0):
                snake_dir = (cell_size, 0)
