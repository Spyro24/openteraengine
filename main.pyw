import pygame as p
import helper

window = p.display.set_mode((500, 300))

div = 40.99999

noise = []
for n in range(500):
    noise.append(helper.perlin.perlin1d(n/div))

for y in range(30):
    for x in range(500):
        noise[x] += helper.perlin.perlin1d(x/div, seed=y)

for y in range(100):
    for x in range(500):
        noise[x] += helper.perlin.perlin1d(x/div, seed=y*y)

for x in range(500):
    window.set_at((x, 150 + noise[x] * 10),(0,255,0))
    
p.display.flip()