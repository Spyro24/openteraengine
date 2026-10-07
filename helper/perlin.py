import math

def perlin2d(x, y, seed=0):
    def gradient(ix, iy):
        # Deterministically map each grid point and seed to an angle
        n = (ix * 374761393 + iy * 668265263 + seed * 1442695041) & 0xFFFFFFFF
        n = ((n ^ (n >> 13)) * 1274126177) & 0xFFFFFFFF
        n ^= n >> 16
        angle = (n / 0xFFFFFFFF) * 2 * math.pi
        return math.cos(angle), math.sin(angle)

    def fade(t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    def dot(ix, iy, dx, dy):
        gx, gy = gradient(ix, iy)
        return gx * dx + gy * dy

    x0, y0 = math.floor(x), math.floor(y)
    dx, dy = x - x0, y - y0
    u, v = fade(dx), fade(dy)

    n00 = dot(x0,     y0,     dx,     dy)
    n10 = dot(x0 + 1, y0,     dx - 1, dy)
    n01 = dot(x0,     y0 + 1, dx,     dy - 1)
    n11 = dot(x0 + 1, y0 + 1, dx - 1, dy - 1)

    nx0 = n00 + (n10 - n00) * u
    nx1 = n01 + (n11 - n01) * u
    return nx0 + (nx1 - nx0) * v

def perlin1d(x, seed=0):
    def gradient(i):
        # Deterministically choose a gradient of -1 or +1
        n = (i * 374761393 + seed * 1442695041) & 0xFFFFFFFF
        n = ((n ^ (n >> 13)) * 1274126177) & 0xFFFFFFFF
        n ^= n >> 16
        return 1.0 if n & 1 else -1.0

    def fade(t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    x0 = math.floor(x)
    dx = x - x0

    # Gradient-dot-distance contributions from both endpoints
    left = gradient(x0) * dx
    right = gradient(x0 + 1) * (dx - 1)

    # Smoothly interpolate between them
    t = fade(dx)
    return left + (right - left) * t
