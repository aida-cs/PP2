import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500  
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_RADIUS = 25 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball")

x, y = WIDTH // 2, HEIGHT // 2
SPEED = 20 

running = True
while running:
    screen.fill(WHITE)  

    pygame.draw.circle(screen, RED, (x, y), BALL_RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - SPEED - BALL_RADIUS >= 0:
                y -= SPEED
            elif event.key == pygame.K_DOWN and y + SPEED + BALL_RADIUS <= HEIGHT:
                y += SPEED
            elif event.key == pygame.K_LEFT and x - SPEED - BALL_RADIUS >= 0:
                x -= SPEED
            elif event.key == pygame.K_RIGHT and x + SPEED + BALL_RADIUS <= WIDTH:
                x += SPEED

    pygame.display.flip()

pygame.quit()