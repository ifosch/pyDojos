import numpy as np
import matplotlib.pyplot as plt

def create_world(shape = None, alive = None):
    if shape is None:
        shape = (3, 3)
    world = np.zeros(shape, dtype=int)
    if alive:
        for position in alive:
            world[position[0], position[1]] = 1
    return world

def draw_world(world):
    plt.imshow(world, cmap=plt.cm.Greys, interpolation='nearest')
