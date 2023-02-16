

#def radians(degrees):
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
