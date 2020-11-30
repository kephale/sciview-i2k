# @SciView sv

from net.imglib2 import RealPoint
from jarray import array
import random as random

w = 101
h = w
d = w

num_spots = 10
spotR = 3

def rand_spot():
    coord = [random.randint(spotR, w-spotR), random.randint(spotR, h-spotR), random.randint(spotR, d-spotR)]
    return RealPoint(array(coord, 'd'))

spots = [rand_spot() for k in range(num_spots)]

print(spots)
print(spots[0])

sv.addPointCloud(spots)
