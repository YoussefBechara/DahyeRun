import pygame
import pygame.freetype 
pygame.init()
win = pygame.display.set_mode((1000, 500)) 
GAME_FONT = pygame.freetype.Font("arial.ttf", 24)

x, y, width, height, vel = 50 , 50 , 10 , 60 , 5
x2, y2 = 900, 50
x3, y3 = 450, 200
run = True
is_up = True
is_left = True
vel_ball = vel 
points1 = 0
points2 = 0
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a]) and (x>0) and (x<500):
        x -= vel
    if (keys[pygame.K_d]) and (x < 500 - width):
        x += vel
    if (keys[pygame.K_w]) and (y>0):
        y -= vel
    if keys[pygame.K_s] and y < 500 - height:
        y += vel
    if (keys[pygame.K_LEFT]) and (x2>500):
        x2 -= vel
    if (keys[pygame.K_RIGHT]) and (x2 < 1000 - width) and (x2> 500-width):
        x2 += vel
    if (keys[pygame.K_UP]) and (y2>0):
        y2 -= vel
    if keys[pygame.K_DOWN] and y2 < 500 - height:
        y2 += vel
    if (x3 == x2) and (y2 <=y3 <= y2+height):
        is_left = False
    if (x3 == x) and (y <=y3 <= y+height):
        is_left = True
    if is_left is True:
        x3 += vel_ball
        if x3 == 1000 - 10:
            is_left = False
    else: 
        x3 -= vel_ball
        if x3 == 0:
            is_left = True
    if is_up is True:
        y3 += vel_ball
        if y3 == 500 - 10:
            is_up = False
    else: 
        y3 -= vel_ball
        if y3 == 0:
            is_up = True
    if x3 == 0:
        points2 += 1
    if x3 == 990:
        points1 += 1
    
    text_surface, rect = GAME_FONT.render(f'Player1:{points1} points, WASD', (255, 255, 255))
    text_surface2, rect = GAME_FONT.render(f'Player2:{points2} points, arrows', (255, 255, 255))
    win.blit(text_surface, (0, 10))
    win.blit(text_surface2, (725, 10))
    line = pygame.draw.rect(win, (255, 255, 0), (495, 0, width, 1000))
    player1 = pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))
    player2 = pygame.draw.rect(win, (255, 255, 255), (x2, y2, width, height))
    ball = pygame.draw.rect(win, (255, 255, 255), (x3, y3, 10, 10))
    pygame.display.update()
    win.fill((0, 0, 0))


    #make computer ai
    
