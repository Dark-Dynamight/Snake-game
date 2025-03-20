import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define window size and colors
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)

# Create window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake settings
snake_block = 10
snake_speed = 10

# Font
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

# Function to display score
def show_score(score):
    value = score_font.render(f"Score: {score}", True, WHITE)
    win.blit(value, [10, 10])

# Main function
def game_loop():
    game_over = False
    game_close = False
    
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    
    snake_body = []
    length = 1
    
    food_x = round(random.randrange(0, WIDTH - snake_block) / 10) * 10
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 10) * 10
    
    clock = pygame.time.Clock()
    
    while not game_over:
        while game_close:
            win.fill(BLACK)
            msg = font_style.render("You Lost! Press C-Play Again or Q-Quit", True, RED)
            win.blit(msg, [WIDTH // 6, HEIGHT // 3])
            show_score(length - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = snake_block, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, snake_block
        
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        x += dx
        y += dy
        win.fill(BLACK)
        pygame.draw.rect(win, GREEN, [food_x, food_y, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)
        if len(snake_body) > length:
            del snake_body[0]
        
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True
        
        for segment in snake_body:
            pygame.draw.rect(win, BLUE, [segment[0], segment[1], snake_block, snake_block])
        
        show_score(length - 1)
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 10) * 10
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 10) * 10
            length += 1
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

# Start the game
game_loop()
