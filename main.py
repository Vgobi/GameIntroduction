import pygame
import random

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Comics", 50)
screen = pygame.display.set_mode([800, 600])
image01 = pygame.image.load('chmurka_01.png')
cloud_x = 0
cloud_y = 0
BLACK = 0, 0, 0
RED = 255, 0, 0
WHITE = 255, 255, 255
clock = pygame.time.Clock()
cloud_position = 0
react = [[random.randint(0, 800), 0, True] for _ in range(10)]
left = 10


end_displayd = 0
running = True
while running:

    screen.fill(BLACK)
    #  Eventy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        hit = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = event.pos[0], event.pos[1]
            for rect in react:
                if rect[0] <= pos_x <= rect[0] + 30 and rect[1] <= pos_y <= rect[1] + 30:
                    print("Trafiony")
                    hit = True
                    rect[-1] = False
                    left -= 1
                    print(left)
                    break
            if not hit:
                print("Pudło")

    # Logika

    if not left:
        tesxsurface = font.render("Win", False, WHITE)
        screen.blit(tesxsurface, (0, 0))
        end_displayd += 1

    if left > 0:
        for rec in react:
            if rec[1] > 600:
                textsurface = font.render("Looser", True, WHITE)
                screen.blit(textsurface, (0, 0))
                end_displayd += 1

    if end_displayd > 180:
        running = False

    screen.blit(image01, (cloud_x, cloud_y))  # tutaj tez mozna ustawic tlo
    if cloud_position < 500:
        cloud_x += 1
        cloud_position += 1
    elif 500 <= cloud_position < 1000:
        cloud_x -= 1
        cloud_position += 1
    elif cloud_position >= 1000:
        cloud_position = 0

    # rysowanie kwadratów
    for rec in react:
        if rec[-1]:
            pygame.draw.rect(screen, RED, (rec[0], rec[1], 30, 30))
            rec[1] += 1
            rec[0] += random.randint(-1, 1)
            if rec[0] > 800:
                rec[0] -= 1
            if rec[0] < -30:
                rec[0] += 1

    # update
    clock.tick(60)
    pygame.display.update()

pygame.quit()
