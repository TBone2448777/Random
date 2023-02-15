#Generative Art Project
#Author: Taylor Sloan 1/27/2023
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


# def radians(degrees):
#     """convert degrees to radians"""
#     return math.pi / 180 * degrees


# def blue(scale=0.8):
#     """return the rgb of a shade of blue"""
#     assert 0 <= scale <= 1, f"scale must be between 0 and 1 inclusive, not {scale}"
#     num = int(scale * 255)
#     return (num // 2, 2 * num // 3, num)


# class Node:
#     """create a node"""

#     def __init__(self, x, y, speed, angle):
#         self.x = x
#         self.y = y
#         self.speed = speed
#         self.angle = angle
#         self.dx = math.sin(self.angle) * self.speed
#         self.dy = math.cos(self.angle) * self.speed

#     def move(self):
#         """move the node"""
#         self.x = self.x + self.dx
#         self.y = self.y + self.dy

#     def draw(self):
#         """draw the node to the screen"""
#         pygame.draw.circle(screen, blue(), (int(self.x), int(self.y)), node_radius)

#     def reflect(self):
#         """reflect off a boundary of the screen"""
#         if self.x > winwidth - node_radius:  # right edge
#             self.x = 2 * (winwidth - node_radius) - self.x
#             self.angle = -self.angle
#         elif self.x < node_radius:  # left edge
#             self.x = 2 * node_radius - self.x
#             self.angle = -self.angle
#         if self.y > winheight - node_radius:  # bottom edge
#             self.y = 2 * (winheight - node_radius) - self.y
#             self.angle = math.pi - self.angle
#         elif self.y < node_radius:  # top edge
#             self.y = 2 * node_radius - self.y
#             self.angle = math.pi - self.angle
#         self.dx = math.sin(self.angle) * self.speed
#         self.dy = math.cos(self.angle) * self.speed


# winwidth = 800  # width of window
# winheight = 600  # height of window
# background = (5, 5, 5)  # this is close to black

# # set generative parameters
# num_nodes = 400
# node_radius = 0
# thresh = 1800

# # initialize pygame
# screen = pygame.display.set_mode((winwidth, winheight))
# clock = pygame.time.Clock()
# pygame.init()
# pygame.display.set_caption("Triangles v1")
# pygame.event.set_allowed([pygame.QUIT, pygame.KEYUP, pygame.KEYDOWN])

# # create nodes
# nodes = []
# for i in range(num_nodes):
#     x = random.randint(node_radius, winwidth - node_radius)
#     y = random.randint(node_radius, winheight - node_radius)
#     speed = random.randint(150, 200) / 600
#     angle = radians(random.randint(0, 359))
#     nodes.append(Node(x, y, speed, angle))

# # the game loop: (press q to quit)
# quit = False
# reset = 0
# while not quit:
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             quit = True
#             break
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_q:
#                 quit = True
#                 break
#     if quit:
#         break

#     screen.fill(background)
#     for node in nodes:
#         node.move()
#         node.reflect()
#         node.draw()

#     if reset % 30 == 0:
#         nodes = sorted(nodes, key = lambda node: node.x)
#         listPerNode = []
#         for i, node1 in enumerate(nodes):
#             dictPerNode = {}
#             run = True
#             for node2 in nodes[i:]:
#                 if (node1.x > node2.x - 150):
#                     x1, y1 = node1.x, node1.y
#                     x2, y2 = node2.x, node2.y
#                     d_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
#                     if d_squared < thresh * 2:
#                         dictPerNode[node2] = node1
#                     elif node1.x > node2.x + 150:
#                         break
#             listPerNode.append(dictPerNode)
#         reset += 1
#     for m in range(0, len(listPerNode)):
#         dictPerNode = listPerNode[m]
#         for node1 in dictPerNode:
#             node2 = dictPerNode[node1]
#             x1, y1 = node1.x, node1.y
#             x2, y2 = node2.x, node2.y
#             d_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
#             if d_squared < thresh:
#                 pygame.draw.aaline(
#                     screen, blue((thresh - d_squared) / thresh), (x1, y1), (x2, y2)
#                 )
#     reset += 1

#     clock.tick(120)
#     pygame.display.flip()
#     print(clock.get_fps())

# pygame.quit()
