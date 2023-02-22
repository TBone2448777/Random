# Author: Taylor Sloan
import random, math, pygame

winwidth = 1000
winheight = 250
background = (255, 255, 255)
jumptime = 60
jumpheight = 3
xpos = winwidth/8
ypos = winheight-winheight/3.4
x=3

# Pygame Init
screen = pygame.display.set_mode((winwidth, winheight))
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Google Dino")
pygame.event.set_allowed([pygame.QUIT, pygame.KEYUP, pygame.KEYDOWN])
screen.fill(background)

quit = False
jumpi = 0
characterY = 0
while not quit:
    # Key tracker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit = True
                break
            elif event.key == pygame.K_SPACE and jumpi == 0:
                jumpi = jumptime
    if quit:
        break
    screen.fill(background)
    # Draw Dino
    # pygame.draw.rect(
    #     screen, (0, 0, 0), (winwidth / 8, winheight - winheight / 8 - characterY, winwidth / 25, winheight / 8), 0
    # )
    pygame.draw.polygon(
        screen, (0, 0, 0), ((xpos+15*x, ypos-characterY), (xpos+19*x, ypos-characterY+2*x), (xpos+20*x, ypos-characterY+3*x), (xpos+21*x, ypos-characterY+5*x), (xpos+21*x, ypos-characterY+6*x), (xpos+20*x, ypos-characterY+9*x), (xpos+18*x, ypos-characterY+10*x), (xpos+17*x, ypos-characterY+10*x), (xpos+18*x, ypos-characterY+12*x), (xpos+18*x, ypos-characterY+14*x), (xpos+19*x, ypos-characterY+16*x), (xpos+19*x, ypos-characterY+20*x), (xpos+18*x, ypos-characterY+22*x), (xpos+17*x, ypos-characterY+22*x), (xpos+17*x, ypos-characterY+23*x), (xpos+16*x, ypos-characterY+23*x), (xpos+16*x, ypos-characterY+24*x), (xpos+13*x, ypos-characterY+24*x), (xpos+13*x, ypos-characterY+22*x), (xpos+9*x, ypos-characterY+22*x), (xpos+4*x, ypos-characterY+23*x), (xpos+x, ypos-characterY+22*x), (xpos, ypos-characterY+21*x), (xpos, ypos-characterY+17*x), (xpos+x, ypos-characterY+19*x), (xpos+4*x, ypos-characterY+20*x), (xpos+9*x, ypos-characterY+16*x), (xpos+11*x, ypos-characterY+9*x), (xpos+10*x, ypos-characterY+8*x), (xpos+10*x, ypos-characterY+5*x), (xpos+11*x, ypos-characterY+2*x))
    )
    # Jump Animation
    if jumpi > jumptime/2:
        characterY += jumpheight
        jumpi -= 1
    if 0 < jumpi <= jumptime/2:
        characterY -= jumpheight
        jumpi -= 1
    clock.tick(60)
    pygame.display.flip()
pygame.quit()