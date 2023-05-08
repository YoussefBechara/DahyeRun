import pygame
pygame.init()
def bar_hp():
    screen_width, screen_height = 1000,500
    x, y = 200, 100
    screen = pygame.display.set_mode((screen_width, screen_height))
    bar_width, bar_height = 700, 30
    bg_bar_width, bg_bar_height = bar_width, bar_height

    def draw_bar():
        bg_bar = pygame.draw.rect(screen, (255, 255, 255), (x, y, bg_bar_width, bg_bar_height))
        bar = pygame.draw.rect(screen, (255, 255, 0), (x, y, bar_width, bar_height))
    run = True
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w]):
            bar_width-=10
        draw_bar()
        pygame.display.update()
        screen.fill((0, 0, 0))


    pygame.quit()


l = [[1,2,3,4,5],[2],[3,3],[4,66]]
for r in range(len(l)):
    for c in range(len(l[r])):
        del l[r][c]
print(l)