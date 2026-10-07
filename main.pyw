import random
import pygame as p
import helper

window = p.display.set_mode((500,300))

div = 0.04999

floor = []
for x in range(window.width):
    floor.append(150)

for _ in range(50):
    seed = random.randint(0,0xFFFF)
    newDiv = random.random()*0.01
    for x in range(window.width):
        floor[x] += helper.perlin.perlin1d(x*newDiv, seed=seed)*10

for y in range(window.height):
    for x in range(window.width):
        if y >= floor[x]:
            noise = helper.perlin.perlin2d(x*div,y*div, seed=seed)
            noise2 = helper.perlin.perlin2d(x*div,y*div, seed=seed*seed)
            if noise2 >= 0.1:
                if noise >= 0:
                    window.set_at((x,y), (128, 128, 128))
            else:
                if noise >= min(0, (1*((y-floor[x]))*0.05)-1):
                    window.set_at((x,y), (128, 128, 128))
    p.display.flip()

for y in range(window.height):
    for x in range(window.width):
        if floor[x] <= y <= floor[x] + max(0,helper.perlin.perlin1d(x*newDiv *2, seed=seed*2)*50) + 10 and window.get_at((x,y)) != (0,0,0):
            window.set_at((x,y), (200, 50, 50))
    p.display.flip()
