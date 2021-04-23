import pygame
import random

pygame.init()
W, H = 500, 500
SIZE = (W, H)
sc = pygame.display.set_mode(SIZE)
fps = pygame.time.Clock()
running = True

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
    if keys[pygame.K_SPACE]:
        speed = 30
    if keys[pygame.K_BACKSPACE]:
        speed = 10


        
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
    global satiety
    ltx = x
    lty = y

    for i, j in enumerate(snake_tails):
        _ltx = snake_tails[i][0]
        _lty = snake_tails[i][1]
         
        snake_tails[i][0] = ltx
        snake_tails[i][1] = lty        
        
        ltx = _ltx
        lty = _lty
    
    for t in (snake_tails):
        pygame.draw.rect(sc,(0, 100, 0),[t[0],t[1], 10, 10])
    if satiety > 10:
            for t in (snake_tails):
                pygame.draw.rect(sc,(66, 170, 255),[t[0],t[1], 10, 10])
    if satiety > 20:
            for t in (snake_tails):
                pygame.draw.rect(sc,(248, 24, 148),[t[0],t[1], 10, 10])
    if satiety > 30:
            for t in (snake_tails):
                pygame.draw.rect(sc,(253, 106, 2),[t[0],t[1], 10, 10])
    if satiety > 40:
            for t in (snake_tails):
                pygame.draw.rect(sc,(255, 211, 0),[t[0],t[1], 10, 10])
    if satiety > 50:
            for t in (snake_tails):
                pygame.draw.rect(sc,(125, 0, 0),[t[0],t[1], 10, 10])
    if satiety > 60:
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
x_a = round(random.randrange(0, W - 10) / 10) * 10
y_a = round(random.randrange(0, H - 10) / 10) * 10
x = W / 2 - 10
y = H / 2 - 10
x_change = 0
y_change = 0
speed = 10


snake_tails = []


while running:
    for  i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
    sc.fill((0,0,0))


    move()
    Tail()
    apples()
    delete_tail()
    pygame.draw.rect(sc, (0,255,0), [x, y, 10, 10])

    fps.tick(30)
    pygame.display.update()