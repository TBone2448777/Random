#Authors: Taylor Sloan, Layden Halcomb 
import random, math, pygame
#CHANGABLE
winwidth = 1200
winheight = 900
background = (200, 200, 200)
lineColor = (0, 0, 0)
linewidth = 5
num_nodesL = 100
num_nodesR = 200
node_radius = 1
thresh = 900

#Based off Above Changables- Don't Touch
widthX = winheight/2.5 
positionX = winwidth / 2
positionY = winheight / 2 + widthX
threshSqrRt = math.sqrt(thresh)

#Delta Cube Vertices
px1, px2, px3, px4, px5 = positionX - widthX, positionX-93*widthX/300, positionX, positionX+93*widthX/300, positionX + widthX
py1, py2, py3, py4, py5, py6= positionY, positionY-(widthX/3), positionY - 2*widthX/3, positionY-119*widthX/80, positionY - 5*widthX/3, positionY-widthX*2

#Colors!
def color1(scale=0.8):
    num = int(scale * 255)
    return (255-num, 255-num, 255-num)
def color2(scale=0.8):
    num = int(scale * 255)
    num *= 2
    if num >= 255:
        num = 255
    return (255-num, 255-num, 255-num)

#Begin Pygame
screen = pygame.display.set_mode((winwidth, winheight))
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("DELTA CUBE")
pygame.event.set_allowed([pygame.QUIT, pygame.KEYUP, pygame.KEYDOWN])
screen.fill(background)

#Various Global Variables
leftXVals = {}
leftXValsLow = {}
rightXVals = {}
rightXValsLow = {}

#Define Diagonal Dictionaries
#Left Dictionary
for i in range(int(py6), int(py2)):
    leftXVals[i] = round(3/5*(i-py6))
print(leftXVals)
for i in range(int(py3), int(py2)):
    leftXValsLow[i] = round(3*(i-py3))
print(leftXValsLow)
#Right Dictionary
for i in range(int(py6), int(py2)):
    rightXVals[i] = round(3/5*(i-py6))
print(rightXVals)
for i in range(int(py3), int(py2)):
    rightXValsLow[i] = round(3*(i-py3))
print(rightXValsLow)

#Left Nodes
class NodeL:
    def __init__(self, x, y, speed, angle):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.dx = math.sin(self.angle) * self.speed
        self.dy = math.cos(self.angle) * self.speed
    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
    def draw(self):
        pygame.draw.circle(screen, color1(), (int(self.x), int(self.y)), node_radius)
    def reflect(self):
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

#Right Nodes
class NodeR:
    def __init__(self, x, y, speed, angle):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.dx = math.sin(self.angle) * self.speed
        self.dy = math.cos(self.angle) * self.speed
    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
    def draw(self):
        pygame.draw.circle(screen, color2(), (int(self.x), int(self.y)), node_radius)
    def reflect(self):
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

#Node L Options
nodesL = []
for i in range(num_nodesL):
    x = random.randint(int(round(px2, 0)) + node_radius, int(round(px3, 0)) - node_radius)
    y = random.randint(int(round(py4, 0)) + node_radius, int(round(py3, 0)) - node_radius)
    speed = random.randint(150, 200) / 600
    angle = math.pi / 180 *(random.randint(0, 359))
    nodesL.append(NodeL(x, y, speed, angle))

#Node R Options
nodesR = []
for i in range(num_nodesR):
    x = random.randint(int(round(px3, 0)) - node_radius, int(round(px4, 0)) + node_radius)
    y = random.randint(int(round(py4, 0)) + node_radius, int(round(py3, 0)) - node_radius)
    speed = random.randint(150, 200) / 600
    angle = math.pi / 180 *(random.randint(0, 359))
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
    pygame.draw.polygon(
        screen, (255, 255, 255), ((px1, py2), (px3, py1), (px5, py2), (px5, py5), (px3, py6), (px1, py5))
    )
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
            if (node1.y > node2.y - threshSqrRt):
                x1, y1 = node1.x, node1.y
                x2, y2 = node2.x, node2.y
                d_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if d_squared < thresh:
                    pygame.draw.aaline(
                        screen, color1((thresh - d_squared) / thresh), (x1, y1), (x2, y2)
                    )
            else:
                break
    nodesR = sorted(nodesR, key = lambda node: node.y)
    for i, node1 in enumerate(nodesR):
        for node2 in nodesR[i:]:
            if (node1.x > node2.y - threshSqrRt):
                x1, y1 = node1.x, node1.y
                x2, y2 = node2.x, node2.y
                d_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if d_squared < thresh:
                    pygame.draw.aaline(
                        screen, color2((thresh - d_squared) / thresh), (x1, y1), (x2, y2)
                    )
            else:
                break
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
