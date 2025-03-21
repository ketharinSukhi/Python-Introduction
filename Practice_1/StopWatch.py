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

# Buttons
button_width, button_height = 100, 40
start_button = pygame.Rect(50, 200, button_width, button_height)
stop_button = pygame.Rect(160, 200, button_width, button_height)
reset_button = pygame.Rect(270, 200, button_width, button_height)

def draw_buttons():
    pygame.draw.rect(screen, GREEN, start_button)
    pygame.draw.rect(screen, RED, stop_button)
    pygame.draw.rect(screen, BLUE, reset_button)
    
    start_text = button_font.render("Start", True, WHITE)
    stop_text = button_font.render("Stop", True, WHITE)
    reset_text = button_font.render("Reset", True, WHITE)
    
    screen.blit(start_text, (start_button.x + 25, start_button.y + 10))
    screen.blit(stop_text, (stop_button.x + 30, stop_button.y + 10))
    screen.blit(reset_text, (reset_button.x + 25, reset_button.y + 10))

def main():
    global start_time, elapsed_time, running
    clock = pygame.time.Clock()
    running_game = True

    while running_game:
        screen.fill( )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    if not running:
                        start_time = time.time() - elapsed_time
                        running = True
                elif stop_button.collidepoint(event.pos):
                    if running:
                        elapsed_time = time.time() - start_time
                        running = False
                elif reset_button.collidepoint(event.pos):
                    elapsed_time = 0
                    running = False
        
        if running:
            elapsed_time = time.time() - start_time
        
        timer_text = font.render(f"{elapsed_time:.2f} sec", True, WHITE)
        screen.blit(timer_text, (WIDTH // 3, HEIGHT // 3))
        
        
        draw_buttons()
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()


if __name__ == "__main__":
    main()