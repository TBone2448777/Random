#Author: Taylor Sloan, Layden Halcomb 

import random, math, pygame
winwidth = 800  # width of window
winheight = 600  # height of window
background = (255,255,255)
widthX = 200
positionX = winwidth / 2
positionY = winheight / 1.2

px1 = positionX - widthX
px2 = positionX-93*widthX/300
px3 = positionX
px4 = positionX+93*widthX/300
px5 = positionX + widthX
py1 = positionY
py2 = positionY-(widthX/3)
py3 = positionY - 2*widthX/3
py4 = positionY-119*widthX/80
py5 = positionY - 5*widthX/3
py6 = positionY-widthX*2

screen = pygame.display.set_mode((winwidth, winheight))
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Triangles v1")
pygame.event.set_allowed([pygame.QUIT, pygame.KEYUP, pygame.KEYDOWN])

quit = False
while not quit:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit = True
                break
    if quit:
        break
    screen.fill(background)
    #1 Bottom Right
    pygame.draw.line(
        screen, (0, 0, 0), (px3, py1), (px5, py2)
    )
    #2 Bottom Left
    pygame.draw.line(
        screen, (0, 0, 0), (px3, py1), (px1, py2)
    )
    #3 Right
    pygame.draw.line(
        screen, (0, 0, 0), (px5, py2), (px5, py5)
    )
    #4 Left
    pygame.draw.line(
        screen, (0, 0, 0), (px1, py2), (px1, py5)
    )
    #5 Top Right
    pygame.draw.line(
        screen, (0, 0, 0), (px5, py5), (px3, py6)
    )
    #6 Top Left
    pygame.draw.line(
        screen, (0, 0, 0), (px1, py5), (px3, py6)
    )
    #7 Low Mid Right
    pygame.draw.line(
        screen, (0, 0, 0), (px3, py3), (px5, py2)
    )
    #8 Low Mid Left
    pygame.draw.line(
        screen, (0, 0, 0), (px3, py3), (px1, py2)
    )
    #9 Mid
    pygame.draw.line(
        screen, (0, 0, 0), (px3, py3), (px3, py6)
    )
    #10 Right Diagonal
    pygame.draw.line(
        screen, (0, 0, 0), (px5, py2), (px3, py6)
    )
    #11 Left Diagonal
    pygame.draw.line(
        screen, (0, 0, 0), (px1, py2), (px3, py6)
    )
    #12 High Mid Left
    pygame.draw.line(
        screen, (0, 0, 0), (px1, py5), (px2, py4)
    )
    #13 High Mid Right
    pygame.draw.line(
        screen, (0, 0, 0), (px5, py5), (px4, py4)
    )

    clock.tick(60)
    pygame.display.flip()
    print(clock.get_fps())

pygame.quit()
