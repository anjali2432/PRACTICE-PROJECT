import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the game window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# Set the size of each cell in the game grid
CELL_SIZE = 20

# Set the initial position and length of the snake
snake_x = WINDOW_WIDTH // 2
snake_y = WINDOW_HEIGHT // 2
snake_length = 1

# Set the initial velocity of the snake
velocity_x = 0
velocity_y = 0

# Set the initial position of the food
food_x = random.randrange(0, WINDOW_WIDTH, CELL_SIZE)
food_y = random.randrange(0, WINDOW_HEIGHT, CELL_SIZE)

# Create the game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the title of the game window
pygame.display.set_caption("Snake Game")

# Set the font and size for the game text
font = pygame.font.SysFont(None, 30)

# Define a function to draw the snake
def draw_snake(snake_list):
    for x,y in snake_list:
        pygame.draw.rect(game_window, (0, 255, 0), (x, y, CELL_SIZE, CELL_SIZE))

# Define a function to display the game over message
def game_over_message():
    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    game_window.blit(game_over_text, (WINDOW_WIDTH//2 - 60, WINDOW_HEIGHT//2 - 20))

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity_x = -CELL_SIZE
                velocity_y = 0
            elif event.key == pygame.K_RIGHT:
                velocity_x = CELL_SIZE
                velocity_y = 0
            elif event.key == pygame.K_UP:
                velocity_y = -CELL_SIZE
                velocity_x = 0
            elif event.key == pygame.K_DOWN:
                velocity_y = CELL_SIZE
                velocity_x = 0

    # Update the snake's position
    snake_x += velocity_x
    snake_y += velocity_y

    # Check for collision with the walls
    if snake_x < 0 or snake_x >= WINDOW_WIDTH or snake_y < 0 or snake_y >= WINDOW_HEIGHT:
        game_over_message()
        pygame.display.update()
        pygame.time.wait(2000)
        snake_x = WINDOW_WIDTH // 2
        snake_y = WINDOW_HEIGHT // 2
        snake_length = 1
        velocity_x = 0
        velocity_y = 0
        food_x = random.randrange(0, WINDOW_WIDTH, CELL_SIZE)
        food_y = random.randrange(0, WINDOW_HEIGHT, CELL_SIZE)

    # Check for collision with the food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(0, WINDOW_WIDTH, CELL_SIZE)
        food_y = random.randrange(0, WINDOW_HEIGHT, CELL_SIZE)
        snake_length += 1

    # Create the snake list
    snake_list = []
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    # Draw the snake
    draw_snake(snake_list)

    # Draw the food
    pygame.draw.rect(game_window, (255, 0, 0),(food_x, food_y, CELL_SIZE, CELL_SIZE))
# Update the display
pygame.display.update()

# Set the game's frame rate
pygame.time.Clock().tick(10)
