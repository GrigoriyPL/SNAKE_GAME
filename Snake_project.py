import pygame
import random

pygame.init()
W, H = 500, 500
SIZE = (W, H)
sc = pygame.display.set_mode(SIZE)
fps = pygame.time.Clock()

def move():
    global x, y, x_change, y_change, speed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x_change == 0:
        x_change = -speed
        y_change = 0
    elif keys[pygame.K_RIGHT] and x_change == 0:
        x_change = speed
        y_change = 0
    elif keys[pygame.K_UP]  and y_change == 0:
        y_change = -speed
        x_change = 0
    elif keys[pygame.K_DOWN] and y_change == 0:
        y_change = speed
        x_change = 0


        
    x += x_change
    y += y_change

    if x < - 10:
        x = W
    elif x > W:
        x = 0
    elif y < -10:
        y = H
    elif y > H:
        y = 0
    
def Tail():
    global satiety, color
    ptx = x
    pty = y

    for i, j in enumerate(snake_tails):
        time_ptx = snake_tails[i][0]
        time_pty = snake_tails[i][1]
         
        snake_tails[i][0] = ptx
        snake_tails[i][1] = pty        
        
        ptx = time_ptx
        pty = time_pty
    
    for t in (snake_tails):
        pygame.draw.rect(sc, color,[t[0],t[1], 10, 10])

def tail_color():
    global color, satiety

    if satiety > 5:
        color = (66, 170, 255)
    if satiety > 10:
        color = (248, 24, 148)
    if satiety > 15:
        color = (253, 106, 2)
    if satiety > 20:
        color = (255, 211, 0)
    if satiety > 25:
        color = (100, 0, 0)
    if satiety > 30:
        satiety = 0

def apples():
    global satiety, x_a, y_a

    pygame.draw.rect(sc, (255, 0, 0), [x_a, y_a, 10, 10])
    if x == x_a and y == y_a:
        satiety += 1
        snake_tails.append([x_a, y_a])
        x_a = round(random.randrange(0, W - 10) / 10) * 10
        y_a = round(random.randrange(0, H - 10) / 10) * 10

def delete_tail():
    global x, x_change, y, y_change, snake_tails

    for i, j in enumerate(snake_tails):
        if (x + x_change == snake_tails[i][0]) and (y + y_change == snake_tails[i][1]):
            snake_tails = snake_tails[:i]
            break

satiety = 0
color = (0, 100, 0)
x_a = round(random.randrange(0, W - 10) / 10) * 10
y_a = round(random.randrange(0, H - 10) / 10) * 10
x = W / 2 - 10
y = H / 2 - 10
x_change = 0
y_change = 0
speed = 10
snake_tails = []

running = True

while running:
    for  i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
    sc.fill((0,0,0))
    pygame.display.set_caption("Snake_project")


    move()
    Tail()
    tail_color()
    apples()
    delete_tail()

    pygame.draw.rect(sc, (0,255,0), [x, y, 10, 10])

    fps.tick(30)
    pygame.display.update()