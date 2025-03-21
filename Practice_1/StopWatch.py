import pygame
import time

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stopwatch")
# Font
font = pygame.font.Font(None, 50)
button_font = pygame.font.Font(None, 30)

# Stopwatch Variables
start_time = 0
elapsed_time = 0
running = False

def main():
    global start_time, elapsed_time, running
    clock = pygame.time.Clock()
    running_game = True

if __name__ == "__main__":
    main()