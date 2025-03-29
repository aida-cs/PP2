import pygame
from color_palette import *  # Custom color definitions
import random
import time

# Initialize Pygame
pygame.init()

# Game screen and cell size settings
WIDTH = 600
HEIGHT = 600
CELL = 30

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Font settings for displaying score and level
font = pygame.font.SysFont("Verdana", 24)

# Draw grid lines on the screen
def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

# Helper class to represent grid coordinates
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Snake class
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  # Movement in x
        self.dy = 0  # Movement in y
        self.score = 0
        self.level = 1

    def move(self):
        # Move each segment to the position of the previous one
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        # Move the head
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        # Draw head in red and body in yellow
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        # If head collides with food
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            tail = self.body[-1]
            for _ in range(food.weight):  # Add segments equal to weight
                self.body.append(Point(tail.x, tail.y))
            self.score += food.weight
            if self.score % 4 == 0:
                self.level += 1
            food.generate_random_pos(self.body)

    def hit_wall(self):
        # Collision with wall
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

    def hit_self(self):
        # Collision with itself
        head = self.body[0]
        return any(head.x == seg.x and head.y == seg.y for seg in self.body[1:])

# Food class
class Food:
    def __init__(self):
        self.pos = Point(9, 9)
        self.weight = 1
        self.spawn_time = time.time()

    def draw(self):
        # Change color based on weight
        color = colorGREEN if self.weight == 1 else colorBLUE if self.weight == 2 else colorPURPLE
        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake_body):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if all(segment.x != x or segment.y != y for segment in snake_body):
                self.pos = Point(x, y)
                self.weight = random.choice([1, 2, 3])
                self.spawn_time = time.time()
                break

# Game loop setup
FPS = 5
clock = pygame.time.Clock()
snake = Snake()
food = Food()
food.generate_random_pos(snake.body)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1

    screen.fill(colorBLACK)
    draw_grid()

    snake.move()
    snake.check_collision(food)

    # End game if collision
    if snake.hit_wall() or snake.hit_self():
        print("Game Over!")
        running = False

    # Make food disappear after 5 seconds
    if time.time() - food.spawn_time > 5:
        food.generate_random_pos(snake.body)

    # Update speed depending on level
    FPS = 5 + (snake.level - 1)

    # Draw snake and food
    snake.draw()
    food.draw()

    # Display score and level
    score_text = font.render(f"Score: {snake.score}", True, colorWHITE)
    level_text = font.render(f"Level: {snake.level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()