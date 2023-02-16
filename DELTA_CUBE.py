#Author: Taylor Sloan, Layden Halcomb 
#Constants and Scalable Options
import random, math, pygame
winwidth = 800  # width of window
winheight = 600  # height of window
background = (69, 69, 69) #black 
lineColor = (181, 12, 0)#white
widthX = winheight/2.5 
positionX = winwidth / 2
positionY = winheight / 2 + widthX
linewidth = 5
num_nodesL = 50
num_nodesR = 100
node_radius = 1
thresh = 900

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
    # pygame.draw.circle(
    #     screen, (0,0,0), (px3 - leftXVals[i], i), 5
    # )
print(leftXVals)
leftXValsLow = {}
for i in range(int(py3), int(py2)):
    leftXValsLow[i] = round(3*(i-py3))
    #Draw line for left dictionary
    # pygame.draw.circle(
    #     screen, (0,0,0), (px3 - leftXValsLow[i], i), 5
    # )
print(leftXValsLow)

#Right Dictionary
rightXVals = {}
for i in range(int(py6), int(py2)):
    rightXVals[i] = round(3/5*(i-py6))
    #Draw line for right dictionary
    # pygame.draw.circle(
    #     screen, (0,0,0), (px3 + rightXVals[i], i), 5
    # )
print(rightXVals)
rightXValsLow = {}
for i in range(int(py3), int(py2)):
    rightXValsLow[i] = round(3*(i-py3))
    #Draw line for right dictionary
    # pygame.draw.circle(
    #     screen, (0,0,0), (px3 + rightXValsLow[i], i), 5
    # )
print(rightXValsLow)

def radians(degrees):
    """convert degrees to radians"""
    return math.pi / 180 * degrees

def green(scale=0.8):
    """return the rgb of a shade of blue"""
    assert 0 <= scale <= 1, f"scale must be between 0 and 1 inclusive, not {scale}"
    num = int(scale * 255)
    return (0, 255-num, 0)

def purple(scale=0.8):
    """return the rgb of a shade of blue"""
    assert 0 <= scale <= 1, f"scale must be between 0 and 1 inclusive, not {scale}"
    num = int(scale * 255)
    return (255-num, 0, 255-num)

class NodeL:
    """create a node"""

    def __init__(self, x, y, speed, angle):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.dx = math.sin(self.angle) * self.speed
        self.dy = math.cos(self.angle) * self.speed

    def move(self):
        """move the node"""
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def draw(self):
        """draw the node to the screen"""
        pygame.draw.circle(screen, green(), (int(self.x), int(self.y)), node_radius)

    def reflect(self):
        """reflect off a boundary of the screen"""
        if self.x > px3:  # right edge
            self.x = 2 * (px3) - self.x
            self.dx = -self.dx
        elif self.x < px3 - leftXVals[int(self.y)]:  # left edge
            self.x = 2 * (px3 - leftXVals[int(self.y)]) - self.x
            self.dx = -self.dx
            self.dy = -self.dy
        elif self.y > py3:
            if self.x > px3 - leftXValsLow[int(self.y)]: # bottom right edge
                self.x = 2 * (px3 - leftXValsLow[int(self.y)]) - self.x
                self.dx = -self.dx
                self.dy = -self.dy
        if self.y > py2 - 2:  # bottom edge
            self.y = 2 * (py2 - 2) - self.y
            self.dy = -self.dy
        elif self.y < py6 + 2:  # top edge
            self.y = 2 * (py6 + 2) - self.y
            self.dy = -self.dy

class NodeR:
    """create a node"""

    def __init__(self, x, y, speed, angle):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.dx = math.sin(self.angle) * self.speed
        self.dy = math.cos(self.angle) * self.speed

    def move(self):
        """move the node"""
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def draw(self):
        """draw the node to the screen"""
        pygame.draw.circle(screen, green(), (int(self.x), int(self.y)), node_radius)

    def reflect(self):
        """reflect off a boundary of the screen"""
        if self.x < px3:  # left edge
            self.x = 2 * (px3) - self.x
            self.dx = -self.dx
        elif self.x > px3 + rightXVals[int(self.y)]:  # right edge
            self.x = 2 * (px3 + rightXVals[int(self.y)]) - self.x
            self.dx = -self.dx
            self.dy = -self.dy
        elif self.y > py3:
            if self.x < px3 + rightXValsLow[int(self.y)]: # bottom right edge
                self.x = 2 * (px3 + rightXValsLow[int(self.y)]) - self.x
                self.dx = -self.dx
                self.dy = -self.dy
        if self.y > py2 - 2:  # bottom edge
            self.y = 2 * (py2 - 2) - self.y
            self.dy = -self.dy
        elif self.y < py6 + 2:  # top edge
            self.y = 2 * (py6 + 2) - self.y
            self.dy = -self.dy

#Adjust amount of nodes


#Node L Options
nodesL = []
for i in range(num_nodesL):
    x = random.randint(int(round(px2, 0)) + node_radius, int(round(px3, 0)) - node_radius)
    y = random.randint(int(round(py4, 0)) + node_radius, int(round(py3, 0)) - node_radius)
    speed = random.randint(150, 200) / 600
    angle = radians(random.randint(0, 359))
    nodesL.append(NodeL(x, y, speed, angle))

#Node R Options
nodesR = []
for i in range(num_nodesR):
    x = random.randint(int(round(px3, 0)) - node_radius, int(round(px4, 0)) + node_radius)
    y = random.randint(int(round(py4, 0)) + node_radius, int(round(py3, 0)) - node_radius)
    speed = random.randint(150, 200) / 600
    angle = radians(random.randint(0, 359))
    nodesR.append(NodeR(x, y, speed, angle))

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

    

    for node in nodesL:
        node.move()
        node.reflect()
        node.draw()
    for node in nodesR:
        node.move()
        node.reflect()
        node.draw()

    nodesL = sorted(nodesL, key = lambda node: node.y)
    for i, node1 in enumerate(nodesL):
        for node2 in nodesL[i:]:
            if (node1.x > node2.x - 150):
                x1, y1 = node1.x, node1.y
                x2, y2 = node2.x, node2.y
                d_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if d_squared < thresh:
                    pygame.draw.aaline(
                        screen, green((thresh - d_squared) / thresh), (x1, y1), (x2, y2)
                    )
    nodesR = sorted(nodesR, key = lambda node: node.y)
    for i, node1 in enumerate(nodesR):
        for node2 in nodesR[i:]:
            if (node1.x > node2.x - 150):
                x1, y1 = node1.x, node1.y
                x2, y2 = node2.x, node2.y
                d_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if d_squared < thresh:
                    pygame.draw.aaline(
                        screen, purple((thresh - d_squared) / thresh), (x1, y1), (x2, y2)
                    )

    #1 Bottom Right
    pygame.draw.line(
        screen, (lineColor), (px3, py1), (px5, py2), (linewidth)
    )
    #2 Bottom Left
    pygame.draw.line(
        screen, (lineColor), (px3, py1), (px1, py2), (linewidth)
    )
    #3 Right
    pygame.draw.line(
        screen, (lineColor), (px5, py2), (px5, py5), (linewidth)
    )
    #4 Left
    pygame.draw.line(
        screen, (lineColor), (px1, py2), (px1, py5), (linewidth)
    )
    #5 Top Right
    pygame.draw.line(
        screen, (lineColor), (px5, py5), (px3, py6), (linewidth)
    )
    #6 Top Left
    pygame.draw.line(
        screen, (lineColor), (px1, py5), (px3, py6), (linewidth)
    )
    # 7 Low Mid Right
    pygame.draw.line(
        screen, (lineColor), (px3, py3), (px5, py2), (linewidth)
    )
    #8 Low Mid Left
    pygame.draw.line(
        screen, (lineColor), (px3, py3), (px1, py2), (linewidth)
    )
    # 9 Mid
    pygame.draw.line(
        screen, (lineColor), (px3, py3), (px3, py6), (linewidth)
    )
    # 10 Right Diagonal
    pygame.draw.line(
        screen, (lineColor), (px5, py2), (px3, py6), (linewidth)
    )
    # 11 Left Diagonal
    pygame.draw.line(
        screen, (lineColor), (px1, py2), (px3, py6), (linewidth)
    )
    # 12 High Mid Left
    pygame.draw.line(
        screen, (lineColor), (px1, py5), (px2, py4), (linewidth)
    )
    #13 High Mid Right
    pygame.draw.line(
        screen, (lineColor), (px5, py5), (px4, py4), (linewidth)
    )

    clock.tick(60)
    pygame.display.flip()
    print(clock.get_fps())

pygame.quit()
