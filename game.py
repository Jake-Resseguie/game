import pygame

pygame.init()

screen_x = 800
screen_y = 600

screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Amogus")

x_cord = 500
y_cord = 300

running = True
while running == True:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (255, 255, 255), (x_cord, y_cord, 50, 50))
    if event.type == pygame.QUIT:
        break

    button = pygame.key.get_pressed()

    print(x_cord, y_cord)

    if button[pygame.K_LEFT]:
        x_cord -= 2
    if button[pygame.K_RIGHT]:
        x_cord += 2
    if button[pygame.K_UP]:
        y_cord -= 2
    if button[pygame.K_DOWN]:
        y_cord += 2

    if x_cord > screen_x:
        x_cord = 0
    if y_cord > screen_y:
        y_cord = 0
    if x_cord < 0:
        x_cord = screen_x
    if y_cord < 0:
        y_cord = screen_y


    pygame.time.Clock().tick(120)
    pygame.display.flip()

