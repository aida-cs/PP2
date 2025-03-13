import pygame
import datetime

pygame.init()

clock_img = pygame.image.load("clock.png")
min_hand_img = pygame.image.load("min_hand.png")
sec_hand_img = pygame.image.load("sec_hand.png")

WIDTH, HEIGHT = clock_img.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

CENTER = (WIDTH // 2, HEIGHT // 2)

def blit_rotate(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=center)
    screen.blit(rotated_image, rect.topleft)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    min_angle = -((minutes % 60) * 6 + 48)  
    sec_angle = -((seconds % 60) * 6 - 60)  

    screen.blit(clock_img, (0, 0))
    
    blit_rotate(min_hand_img, min_angle, CENTER)
    blit_rotate(sec_hand_img, sec_angle, CENTER)
    
    pygame.display.flip()
    pygame.time.delay(10) 

pygame.quit()