import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    tool = 'line'  # line, rect, circle, eraser
    drawing = False
    start_pos = None
    points = []

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Color mode selection
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'eraser'

                # Tool selection
                if event.key == pygame.K_1:
                    tool = 'line'
                elif event.key == pygame.K_2:
                    tool = 'rect'
                elif event.key == pygame.K_3:
                    tool = 'circle'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    if tool == 'line':
                        points.append(start_pos)
                        points = points[-256:]
                elif event.button == 3:
                    radius = max(1, radius - 1)  # Right click shrinks
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    end_pos = event.pos
                    drawing = False
                    if tool == 'rect':
                        draw_rect(screen, start_pos, end_pos, radius, mode)
                    elif tool == 'circle':
                        draw_circle(screen, start_pos, end_pos, radius, mode)
            elif event.type == pygame.MOUSEMOTION:
                if tool == 'line' and drawing:
                    position = event.pos
                    points.append(position)
                    points = points[-256:]

        if tool == 'line':
            screen.fill((0, 0, 0))
            for i in range(len(points) - 1):
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
        pygame.display.flip()
        clock.tick(60)

def get_color(index, mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    if mode == 'blue':
        return (c1, c1, c2)
    elif mode == 'red':
        return (c2, c1, c1)
    elif mode == 'green':
        return (c1, c2, c1)
    elif mode == 'eraser':
        return (0, 0, 0)
    return (255, 255, 255)

def drawLineBetween(screen, index, start, end, width, color_mode):
    color = get_color(index, color_mode)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def draw_rect(screen, start, end, width, mode):
    color = get_color(255, mode)
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                       abs(start[0] - end[0]), abs(start[1] - end[1]))
    pygame.draw.rect(screen, color, rect, width)

def draw_circle(screen, start, end, width, mode):
    color = get_color(255, mode)
    center = start
    radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
    pygame.draw.circle(screen, color, center, radius, width)

main()

#functions:
#R	Red color
#G	Green color
#B	Blue color
#E	Eraser (black)
#1	Line tool (default)
#2	Rectangle tool
#3	Circle tool
#Left Click	Start drawing
#Right Click	Decrease brush size
#Scroll	(optional to implement grow)