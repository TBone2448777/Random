#Author: Taylor Sloan, Layden Halcomb 
#Constants and Scalable Options
import random, math, pygame
winwidth = 800  # width of window
winheight = 600  # height of window
background = (255,255,255) #white 
widthX = winheight/2.5 
positionX = winwidth / 2
positionY = winheight / 2 + widthX
linewidth = 5

#Various vertices around the DELTA CUBE
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

#Set Up Pygame
screen = pygame.display.set_mode((winwidth, winheight))
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("DELTA CUBE")
pygame.event.set_allowed([pygame.QUIT, pygame.KEYUP, pygame.KEYDOWN])
screen.fill(background)

#Left Dictionary
leftXVals = {}
for i in range(int(py6), int(py2)):
    leftXVals[i] = round(3/5*(i-py6))
    #Draw line for left dictionary
    pygame.draw.circle(
        screen, (0,0,0), (px3 - leftXVals[i], i), 5
    )
print(leftXVals)

def radians(degrees):
    """convert degrees to radians"""
    return math.pi / 180 * degrees


def blue(scale=0.8):
    """return the rgb of a shade of blue"""
    assert 0 <= scale <= 1, f"scale must be between 0 and 1 inclusive, not {scale}"
    num = int(scale * 255)
    return (num // 2, 2 * num // 3, num)

class NodeL:
    """create a node"""

    def __init__(self, x, y, speed, angle):
        self.x = x
        self.y = y
        self.speed = 2
        self.angle = angle
        self.dx = math.sin(self.angle) * self.speed
        self.dy = math.cos(self.angle) * self.speed

    def move(self):
        """move the node"""
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def draw(self):
        """draw the node to the screen"""
        pygame.draw.circle(screen, blue(), (int(self.x), int(self.y)), node_radius)

    def reflect(self):
        """reflect off a boundary of the screen"""
        if self.x > px3:  # right edge
            self.x = 2 * (px3) - self.x
            self.angle = -self.angle
        elif self.x < px3 - leftXVals[int(self.y)]:  # left edge
            self.x = 2 * (px3 - leftXVals[int(self.y)]) - self.x
            self.angle = -self.angle
        if self.y > py2 - 2:  # bottom edge
            self.y = 2 * (py2 - 2) - self.y
            self.angle = math.pi -self.angle
        elif self.y < py6 + 2:  # top edge
            self.y = 2 * (py6 + 2) - self.y
            self.angle = math.pi -self.angle
        self.dx = math.sin(self.angle) * self.speed
        self.dy = math.cos(self.angle) * self.speed

#Adjust amount of nodes
num_nodes = 50
node_radius = 1
thresh = 1800

#Node L Options
nodesL = []
for i in range(num_nodes):
    x = random.randint(int(round(px2, 0)) + node_radius, int(round(px3, 0)) - node_radius)
    y = random.randint(int(round(py4, 0)) + node_radius, int(round(py3, 0)) - node_radius)
    speed = random.randint(150, 200) / 600
    angle = radians(random.randint(0, 359))
    nodesL.append(NodeL(x, y, speed, angle))


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

    # screen.fill(background)

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

    for node in nodesL:
        node.move()
        node.reflect()
        node.draw()

    clock.tick(60)
    pygame.display.flip()
    print(clock.get_fps())

pygame.quit()
