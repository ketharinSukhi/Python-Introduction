import pygame 
import random

pygame.init()

# Constants
width, height = 600, 400
cell_size = 30
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# Game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SNAKE GAME")

# Snake initialization
snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (cell_size, 0)

def generate_food():
    while True:
        food = (random.randint(0, (width // cell_size)-1) * cell_size,
                random.randint(0, (height // cell_size)-1) * cell_size)
        if food not in snake:  # Ensure food is not inside the snake
            return food

# Food initialization
food = generate_food()

clock = pygame.time.Clock()
score = 0
running = True

font = pygame.font.Font(None, 36)

def draw_score():
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

def game_over():
    screen.fill(black)
    text = font.render("Game Over! Press any key to exit", True, red)
    screen.blit(text, (width // 6, height // 2))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    exit()

while running:
    screen.fill(black)

    # Event handling
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
    
    # Move snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Check for collisions
    if new_head in snake or new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
        game_over()
    
    snake.insert(0, new_head)
    
    # Check if food is eaten
    if new_head == food:
        score += 1
        food = generate_food()
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], cell_size, cell_size))

    # Draw food
    pygame.draw.rect(screen, red, (food[0], food[1], cell_size, cell_size))

    # Draw score
    draw_score()
    
    pygame.display.flip()
    clock.tick(7)

pygame.quit()
