#Author: Taylor Sloan, Layden Halcomb 
import random, math, pygame
winwidth = 800  # width of window
winheight = 600  # height of window
background = (255,255,255)
widthX = 200
positionX = winwidth / 2
positionY = winheight / 1.2
linewidth = 5

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
pygame.display.set_caption("DELTA CUBE")
pygame.event.set_allowed([pygame.QUIT, pygame.KEYUP, pygame.KEYDOWN])
screen.fill(background)
leftXVals = {}
for i in range(0, int(round(5*widthX/3, 0))):
    leftXVals[i] = round(5/3*i)
    print(str(i + widthX) + ", " + str(leftXVals[i]))
    pygame.draw.circle(
        screen, (0,0,0), (i + widthX, leftXVals[i]), 5
    )

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
    #1 Bottom Right
    pygame.draw.line(
        screen, (0, 0, 0), (px3, py1), (px5, py2), (linewidth)
    )
    #2 Bottom Left
    pygame.draw.line(
        screen, (0, 0, 0), (px3, py1), (px1, py2), (linewidth)
    )
    #3 Right
    pygame.draw.line(
        screen, (0, 0, 0), (px5, py2), (px5, py5), (linewidth)
    )
    #4 Left
    pygame.draw.line(
        screen, (0, 0, 0), (px1, py2), (px1, py5), (linewidth)
    )
    #5 Top Right
    pygame.draw.line(
        screen, (0, 0, 0), (px5, py5), (px3, py6), (linewidth)
    )
    #6 Top Left
    pygame.draw.line(
        screen, (0, 0, 0), (px1, py5), (px3, py6), (linewidth)
    )
    #7 Low Mid Right
    pygame.draw.line(
        screen, (0, 0, 0), (px3, py3), (px5, py2), (linewidth)
    )
    #8 Low Mid Left
    pygame.draw.line(
        screen, (0, 0, 0), (px3, py3), (px1, py2), (linewidth)
    )
    #9 Mid
    pygame.draw.line(
        screen, (0, 0, 0), (px3, py3), (px3, py6), (linewidth)
    )
    #10 Right Diagonal
    pygame.draw.line(
        screen, (0, 0, 0), (px5, py2), (px3, py6), (linewidth)
    )
    #11 Left Diagonal
    pygame.draw.line(
        screen, (0, 0, 0), (px1, py2), (px3, py6), (linewidth)
    )
    #12 High Mid Left
    pygame.draw.line(
        screen, (0, 0, 0), (px1, py5), (px2, py4), (linewidth)
    )
    #13 High Mid Right
    pygame.draw.line(
        screen, (0, 0, 0), (px5, py5), (px4, py4), (linewidth)
    )

    clock.tick(60)
    pygame.display.flip()
    print(clock.get_fps())

pygame.quit()
