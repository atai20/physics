import pygame
import math
t = 0
g = 9.8
class Object:
    def __init__(self, x, y, m, wide):
        self.x = x
        self.y = y
        self.m = m
        self.wide = wide
        self.angle = 0
        self.ground_y = 400
        self.f = 0
        self.obj = pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, 50, 50))
        self.ground = pygame.draw.rect(win, (255, 255, 255), (0, self.ground_y, 500, 500))


    def draw(self):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, 50, 50), 1)
        pygame.draw.rect(win, (255, 255, 255), (0, self.ground_y, 500, 500), 1)


class Objects():
    def __init__(self):
        self.objects = []

    def create_obj(self, *objects):
        for obj in objects:
            self.objects.append(obj)

    def go_to(self, obj,  *direct):

        index = self.objects.index(obj)
        self.objects[index].obj = pygame.draw.rect(win, (255, 255, 255), (self.objects[index].x, self.objects[index].y, 50, 50), 1)

        for d in range(len(direct)):
            self.objects[index].f = direct[d][1]
            self.objects[index].angle = direct[d][0]
            self.objects[index].x += self.objects[index].f * math.cos(self.objects[index].angle)
            self.objects[index].y += self.objects[index].f * math.sin(self.objects[index].angle)

        self.objects[index].draw()

    def being(self, obj, t):
        index = self.objects.index(obj)

        self.Vg = (math.pi/2, (t**2*g)/2)
        self.Fgrav = (math.pi/2, self.objects[index].m*g)
        self.P = (math.pi/2, self.objects[index].m*g)
        
        if self.objects[index].obj.colliderect(self.objects[index].ground):
            self.Vg = (0, 0)

        self.go_to(obj, (self.Vg))




pygame.init()

clock = pygame.time.Clock()

win = pygame.display.set_mode((500, 480))
run = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
d1 = 2
d = Object(100, 100, 2, 1)
Objcts = Objects()
Objcts.create_obj(d)
s = 0.1
while run:
    t+=0.0004
    win.fill(BLACK)

    fall = (0, (g * t ** 2) / 2)

    Objcts.being(d, t)



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False