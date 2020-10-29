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
        self.main_F = (0, 0)
        self.ground_y = 400
        self.obj = pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, 50, 50))
        self.ground = pygame.draw.rect(win, (255, 255, 255), (0, self.ground_y, 500, 500))
        #object data

    def draw(self):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, 50, 50), 1)


class Objects():
    def __init__(self):
        self.objects = []

    def create_obj(self, *objects):
        for obj in objects:
            self.objects.append(obj)

    def go_to(self, obj, *direct):

        index = self.objects.index(obj)
        self.objects[index].obj = pygame.draw.rect(win, (255, 255, 255),
                                                   (self.objects[index].x, self.objects[index].y, 50, 50), 1)

        for d in range(len(direct)):
            self.objects[index].f = direct[d][1]
            if direct[d][0]==0:
                self.objects[index].main_F = (direct[d][0], direct[d][1])
            else:
                self.objects[index].main_F = (2*math.pi, direct[d][1])

            self.objects[index].x += self.objects[index].f * math.cos(direct[d][0])
            self.objects[index].y += self.objects[index].f * math.sin(direct[d][0])


        self.objects[index].draw()

    def being(self, t, *obj):

        for object in obj:

            object.index = self.objects.index(object)
            object.Vg = (math.pi / 2, (t ** 2 * g) / 2)
            object.Fgrav = (math.pi / 2, self.objects[object.index].m * g)

            for objct1 in self.objects:
                for objct2 in obj:
                    if objct2.obj.colliderect(objct1.obj) and objct2 != objct1:
                        if objct1.main_F[0]==objct2.main_F[0]:
                            objct2.P = (objct2.main_F[0], (2*objct1.m * objct1.f + objct2.f*(objct2.m - objct1.m) )/objct2.m + objct1.m)
                        else:
                            objct2.P = (objct2.main_F[0]-math.pi, (2*objct1.m * objct1.f + objct2.f*(objct2.m - objct1.m) )/objct2.m + objct1.m)

            print(str(obj[0].main_F[0])+' '+str(obj[0].m))
            print(str(obj[1].main_F[0])+' '+str(obj[1].m))


            self.go_to(object, (0, 0))

        self.go_to(obj[0], obj[0].P)
        self.go_to(obj[1], obj[1].P)




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
d = Object(100, 200, 0.02, 1)
d2 = Object(250, 200, 0.02, 1)
d.P = (2*math.pi, 0.04)
d2.P = (2*math.pi, 0.01)
Objcts = Objects()
Objcts.create_obj(d)
Objcts.create_obj(d2)
s = 0.1
while run:
    t += 0.0004
    win.fill(BLACK)

    fall = (0, (g * t ** 2) / 2)

    Objcts.being(t, d, d2)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False