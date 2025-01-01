import math
import random

p = [151,160,137,91,90,15,131,13,201,95,96,53,194,233,7,225,
     140,36,103,30,69,142,8,99,37,240,21,10,23,190,6,148,
     247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,
     57,177,33,88,237,149,56,87,174,20,125,136,171,168,68,175,
     74,165,71,134,139,48,27,166,77,146,158,231,83,13,53,231,
     81,111,74,30,68,17,19,23,99,40,142,51,72,39,52,83,
     83,190,30,90,45,190,117,45,123,51,89,120,30,118,0,93,
     156,245,105,14,234,119,1,233,99,252,219,55,170,77,4,37]
p = p + p

def lerp(a, b, t):
    return a + t * (b - a)

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def grad(hash, x, y):
    h = hash & 15
    u = x if h < 8 else y
    v = y if h < 4 else x
    return (u + v) if (h & 1) == 0 else -(u + v)

def perlin(x, y, noise_scale=1.0):
    xi = int(x) & 255
    yi = int(y) & 255
    xf = x - int(x)
    yf = y - int(y)
    u = fade(xf)
    v = fade(yf)
    
    aa = p[p[xi] + yi]
    ab = p[p[xi] + yi + 1]
    ba = p[p[xi + 1] + yi]
    bb = p[p[xi + 1] + yi + 1]

    x1 = lerp(grad(aa, xf, yf), grad(ba, xf - 1, yf), u)
    x2 = lerp(grad(ab, xf, yf - 1), grad(bb, xf - 1, yf - 1), u)
    
    return lerp(x1, x2, v) * noise_scale

def ascii_perlin(width, height, scale=10, chars=" .:-=+*%@#", noise_scale=1.0):
    output = []
    for y in range(height):
        row = []
        for x in range(width):
            noise_value = perlin(x / scale, y / scale, noise_scale)
            char_index = int((noise_value + 1) / 2 * (len(chars) - 1))
            row.append(chars[char_index])
        output.append("".join(row))
    return "\n".join(output)

width, height = 80, 40
noise_scale = float(input("Enter the noise scale: "))
ascii_image = ascii_perlin(width, height, scale=30, noise_scale=noise_scale)
print(ascii_image)
