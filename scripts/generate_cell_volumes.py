# @SciView sv

import net.imglib2.img.array.ArrayImgs as ArrayImgs
import bdv.util.BdvFunctions as BdvFunctions
import random as random

w = 50
h = w
d = w
tmax = 10

num_spots = 10
spotR = 3

img = ArrayImgs.unsignedBytes(w, h, d, tmax)

def rand_spot():
    return [random.randint(spotR, w-spotR), random.randint(spotR, h-spotR), random.randint(spotR, d-spotR)]

spots = [rand_spot() for k in range(num_spots)]

print(spots)

img_ra = img.randomAccess()

spotR2 = spotR**2

for spot in spots:
    x = spot[0]
    y = spot[1]
    z = spot[2]
    for t in range(0, tmax):
        # Apply velocity after first timestep
        if (t > 0):
            nbr = random.choice(spots)
            if (x - nbr[0]) < 0:
                x += 1
            else:
                x -= 1
            if (y - nbr[1]) < 0:
                y += 1
            else:
                y -= 1
            if (z - nbr[2]) < 0:
                z += 1
            else:
                z -= 1
        for xo in range(-spotR, spotR + 1):
            for yo in range(-spotR, spotR + 1):
                for zo in range(-spotR, spotR + 1):
                    dx = x + xo
                    dy = y + yo
                    dz = z + zo
                    # Make a sphere
                    #print([( xo*xo + yo*yo + zo*zo ), xo, yo, zo, spotR2])
                    if ( xo*xo + yo*yo + zo*zo ) < spotR2:
                        img_ra.setPosition(dx, 0)
                        img_ra.setPosition(dy, 1)
                        img_ra.setPosition(dz, 2)
                        img_ra.setPosition(t, 3)
                        img_ra.get().setReal(255)

print('done')
BdvFunctions.show(img, "test")

sv.addVolume(img)
