# @UIService ui

import net.imglib2.img.array.ArrayImgs as ArrayImgs
import bdv.util.BdvFunctions as BdvFunctions

import random as random

w = 101
h = w
d = w

img = ArrayImgs.unsignedBytes(w, h, d)
img_ra = img.randomAccess()

for x in range(0, w):
    for y in range(0, h):
        for z in range(0, d):
            img_ra.setPosition(x, 0)
            img_ra.setPosition(y, 1)
            img_ra.setPosition(z, 2)

            xo = x - 50
            yo = y - 50
            zo = z - 50

            val = 255 - ( xo**2 + yo**2 + zo**2 ) ** 0.65

            img_ra.get().setReal(int(val))

print('done')

ui.show("test_volume", img)
