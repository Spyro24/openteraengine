import pygame as p
import helper

window = p.display.set_mode((0,0))

div = 0.04999

for y in range(window.height):
    for x in range(window.width):
        window.set_at((x,y), (0, 127 * helper.perlin.perlin2d(x*div,y*div) + 127, 0))
    p.display.flip()

for y in range(window.height):
    for x in range(window.width):
        px = window.get_at((x,y))
        window.set_at((x,y), (0, px[1], 127 * helper.perlin.perlin2d(x*div,y*div, seed=50493) + 127))
    p.display.flip()

for y in range(window.height):
    for x in range(window.width):
        px = window.get_at((x,y))
        window.set_at((x,y), (127 * helper.perlin.perlin2d(x*div,y*div, seed=76281) + 127, px[1], px[2]))
    p.display.flip()