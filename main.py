import pygame
import math

t = 0


def vector_sum(obj, direct):
    for d in range(len(direct)):
        obj.v_vel = direct[d][1]

        if direct[d][0] != 0:
            obj.main_v = (direct[d][0], direct[d][1])
        else:
            obj.main_v = (2 * math.pi, direct[d][1])

        obj.x += obj.v_vel * math.cos(direct[d][0])
        obj.y += obj.v_vel * math.sin(direct[d][0])

class Object:
    def __init__(self, x, y, m, wide):
        self.x = x
        self.y = y
        self.m = m
        self.wide = wide
        self.main_v = (0, 0)
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


        vector_sum(self.objects[index], direct)

        self.objects[index].draw()

    def being(self, t, *obj):

        for object in obj:

            object.index = self.objects.index(object)


            for objct2 in self.objects:
                for objct1 in obj:
                    if objct1.obj.colliderect(objct2.obj) and objct1 != objct2:
                        self.go_to(objct1, (2*objct2.main_v[0], 1))
                        print(objct2.main_v[0])





            print(str(obj[0].main_v[0])+' '+str(obj[0].m))
            print(str(obj[1].main_v[0])+' '+str(obj[1].m))


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
d.P = (0, 0.04)
d2.P = (math.pi, 0.04)
Objcts = Objects()
Objcts.create_obj(d)
Objcts.create_obj(d2)
s = 0.1
while run:
    t += 0.0004
    win.fill(BLACK)


    Objcts.being(t, d, d2)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False