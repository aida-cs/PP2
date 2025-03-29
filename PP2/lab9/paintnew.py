import pygame
import math

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
screen.fill((0, 0, 0))
base_layer.blit(screen, (0, 0))
pygame.display.set_caption("Shape Drawer with Brush and Eraser")

# Colors
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
current_color = colorRED  # Default

# Clock and brush settings
clock = pygame.time.Clock()
LMBpressed = False
THICKNESS = 5

# Tool settings
figures = ['Brush', 'Line', 'Rectangle', 'Square', 'Right Triangle', 'Equilateral Triangle', 'Rhombus']
figure_index = 0  # Brush is default

# Previous and current mouse position
prev_pos = (0, 0)
curr_pos = (0, 0)

# Helper functions
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_figure(figure_index):
    x1, y1 = prev_pos
    x2, y2 = curr_pos
    if figures[figure_index] == 'Line':
        pygame.draw.line(screen, current_color, (x1, y1), (x2, y2), THICKNESS)
    elif figures[figure_index] == 'Rectangle':
        pygame.draw.rect(screen, current_color, calculate_rect(x1, y1, x2, y2), THICKNESS)
    elif figures[figure_index] == 'Square':
        side = max(abs(x2 - x1), abs(y2 - y1))
        rect = pygame.Rect(x1, y1, side if x2 >= x1 else -side, side if y2 >= y1 else -side)
        rect.normalize()
        pygame.draw.rect(screen, current_color, rect, THICKNESS)
    elif figures[figure_index] == 'Right Triangle':
        pygame.draw.polygon(screen, current_color, [(x1, y1), (x1, y2), (x2, y2)], THICKNESS)
    elif figures[figure_index] == 'Equilateral Triangle':
        height = math.sqrt(3) / 2 * abs(x2 - x1)
        top_x = (x1 + x2) / 2
        top_y = y1 - height if y2 < y1 else y1 + height
        pygame.draw.polygon(screen, current_color, [(x1, y2), (x2, y2), (top_x, top_y)], THICKNESS)
    elif figures[figure_index] == 'Rhombus':
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        dx = abs(x2 - x1) // 2
        dy = abs(y2 - y1) // 2
        pygame.draw.polygon(screen, current_color, [
            (center_x, y1),
            (x2, center_y),
            (center_x, y2),
            (x1, center_y)
        ], THICKNESS)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse input
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prev_pos = event.pos
            curr_pos = event.pos

        elif event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                curr_pos = event.pos
                if figures[figure_index] == 'Brush':
                    pygame.draw.line(screen, current_color, prev_pos, curr_pos, THICKNESS)
                    base_layer.blit(screen, (0, 0))
                    prev_pos = curr_pos

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            curr_pos = event.pos
            if figures[figure_index] != 'Brush':
                draw_figure(figure_index)
                base_layer.blit(screen, (0, 0))

        # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS or event.key == pygame.K_KP_PLUS:
                THICKNESS += 1
                print(f"Increased thickness to {THICKNESS}")
            if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
                print(f"Reduced thickness to {THICKNESS}")
            if event.key == pygame.K_UP:
                figure_index = (figure_index + 1) % len(figures)
                print(f"Selected tool: {figures[figure_index]}")
            if event.key == pygame.K_DOWN:
                figure_index = (figure_index - 1) % len(figures)
                print(f"Selected tool: {figures[figure_index]}")
            if event.key == pygame.K_r:
                current_color = colorRED
                print("Changed color to RED")
            if event.key == pygame.K_g:
                current_color = colorGREEN
                print("Changed color to GREEN")
            if event.key == pygame.K_b:
                current_color = colorBLUE
                print("Changed color to BLUE")
            if event.key == pygame.K_e:
                screen.fill((0, 0, 0))
                base_layer.fill((0, 0, 0))
                print("Screen cleared")

    screen.blit(base_layer, (0, 0))

    if LMBpressed and figures[figure_index] != 'Brush':
        draw_figure(figure_index)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()