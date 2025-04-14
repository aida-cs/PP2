import pygame
import random
import time
import psycopg2
from datetime import datetime

# Colors
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorGRAY = (150, 150, 150)
colorRED = (255, 0, 0)
colorYELLOW = (255, 255, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorPURPLE = (160, 32, 240)
colorWALL = (139, 69, 19)

# Pygame init
pygame.init()
WIDTH, HEIGHT, CELL = 600, 600, 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Verdana", 24)
clock = pygame.time.Clock()

# DB setup
def connect_to_db():
    try:
        return psycopg2.connect(host="localhost", database="postgres", user="postgres", password="650280")
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# Save score to database
def save_score(name, score, level):
    conn = connect_to_db()
    if conn:
        with conn.cursor() as cur:
            # Ensure the user exists in the 'users' table
            cur.execute("INSERT INTO users(name) VALUES(%s) ON CONFLICT DO NOTHING", (name,))
            
            # Insert or update the score and level in the 'user_score' table
            cur.execute("""
                INSERT INTO user_score(name, score, level)
                VALUES(%s, %s, %s)
                ON CONFLICT (name) 
                DO UPDATE SET score = EXCLUDED.score, level = EXCLUDED.level;
            """, (name, score, level))
            conn.commit()
            conn.close()

# Get last score of the player
def get_last_score(name):
    conn = connect_to_db()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT score, level FROM user_score WHERE name = %s ORDER BY id DESC LIMIT 1", (name,))
            result = cur.fetchone()
            conn.close()
            if result:
                return result  # (score, level)
            else:
                return (0, 1)  # Default score and level if no previous score found
    return (0, 1)

# Menu screen
def show_menu():
    screen.fill(colorBLACK)
    title_text = font.render("Snake Game", True, colorWHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
    pygame.draw.rect(screen, colorWHITE, input_box, 2)

    start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
    pygame.draw.rect(screen, colorWHITE, start_button, 2)

    start_text = font.render("Start", True, colorWHITE)
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 65))

    pygame.display.flip()

    return input_box, start_button

# Text input
def get_username(input_box):
    username = ''
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif event.key == pygame.K_RETURN and username != '':
                    active = False
                else:
                    username += event.unicode

        screen.fill(colorBLACK)
        pygame.draw.rect(screen, colorWHITE, input_box, 2)

        username_text = font.render(username, True, colorWHITE)
        screen.blit(username_text, (input_box.x + 5, input_box.y + 5))

        pygame.display.flip()

    return username

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0
        self.score, self.level = 0, 1
    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy
    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x*CELL, self.body[0].y*CELL, CELL, CELL))
        for s in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (s.x*CELL, s.y*CELL, CELL, CELL))
    def grow(self, weight):
        tail = self.body[-1]
        for _ in range(weight):
            self.body.append(Point(tail.x, tail.y))
    def hit_wall(self):
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL
    def hit_self(self):
        head = self.body[0]
        return any(head.x == s.x and head.y == s.y for s in self.body[1:])

def draw_grid():
    for i in range(WIDTH // CELL):
        for j in range(HEIGHT // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Food:
    def __init__(self):
        self.pos = Point(5, 5)
        self.weight = 1
        self.spawn_time = time.time()
    def generate(self, snake, walls):
        while True:
            x, y = random.randint(0, WIDTH//CELL-1), random.randint(0, HEIGHT//CELL-1)
            if all(p.x != x or p.y != y for p in snake.body) and all(w.x != x or w.y != y for w in walls):
                self.pos = Point(x, y)
                self.weight = random.choice([1, 2, 3])
                self.spawn_time = time.time()
                break
    def draw(self):
        color = colorGREEN if self.weight == 1 else colorBLUE if self.weight == 2 else colorPURPLE
        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

def generate_walls(count):
    return [Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1)) for _ in range(count)]

def draw_walls(walls):
    for w in walls:
        pygame.draw.rect(screen, colorWALL, (w.x * CELL, w.y * CELL, CELL, CELL))

def game_loop(username):
    snake = Snake()
    food = Food()
    walls = []
    snake.level, snake.score = get_last_score(username)
    food.generate(snake, walls)

    running = True
    paused = False
    FPS = 5 + (snake.level - 1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pause the game
                    paused = not paused
                    if paused:
                        save_score(username, snake.score, snake.level)  # Save progress on pause
                        print("Game Paused. Progress saved.")
                if not paused:
                    if event.key == pygame.K_RIGHT and snake.dx != -1:
                        snake.dx, snake.dy = 1, 0
                    elif event.key == pygame.K_LEFT and snake.dx != 1:
                        snake.dx, snake.dy = -1, 0
                    elif event.key == pygame.K_UP and snake.dy != 1:
                        snake.dx, snake.dy = 0, -1
                    elif event.key == pygame.K_DOWN and snake.dy != -1:
                        snake.dx, snake.dy = 0, 1

        if paused:
            continue

        screen.fill(colorBLACK)
        draw_grid()

        snake.move()

        if snake.body[0].x == food.pos.x and snake.body[0].y == food.pos.y:
            snake.grow(food.weight)
            snake.score += food.weight
            food.generate(snake, walls)
            if snake.level == 2 and snake.score % 5 == 0:
                FPS += 1
            if snake.level < 5:
                snake.level = min(5, 1 + snake.score // 5)
            if snake.level >= 4:
                walls = generate_walls(10)

        if time.time() - food.spawn_time > 5:
            food.generate(snake, walls)

        if snake.hit_wall() or snake.hit_self() or any(snake.body[0].x == w.x and snake.body[0].y == w.y for w in walls):
            save_score(username, snake.score, snake.level)
            print("Game Over!")
            break

        FPS = 5 + (snake.level - 1)

        snake.draw()
        food.draw()
        if snake.level >= 4:
            draw_walls(walls)

        score_text = font.render(f"Score: {snake.score}", True, colorWHITE)
        level_text = font.render(f"Level: {snake.level}", True, colorWHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (WIDTH - 150, 10))

        pygame.display.flip()
        clock.tick(FPS)

def main():
    input_box, start_button = show_menu()
    name = get_username(input_box)

    if name:
        game_loop(name)

if __name__ == "__main__":
    main()