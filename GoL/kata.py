import numpy as np

def cutting_matrix(x, y, shape = None):
    if shape is None:
        shape = (3, 3)
    rs = [[x2, x2] for x2 in [x - 1, x, x + 1] if x2 >= 0 and x2 < shape[0]]
    cs = [[y2 for y2 in [y - 1, y, y + 1] if y2 >= 0 and y2 < shape[1]]] * len(rs)
    for i, r in enumerate(rs):
        if len(r) < len(cs[0]):
            rs[i] = [r[0]] * len(cs[0])
    return rs, cs

def alive(world, x, y):
    rs, cs = cutting_matrix(x, y, shape=world.shape)
    rows = np.array(rs, dtype=np.intp)
    columns = np.array(cs, dtype=np.intp)
    total = world[rows,columns].sum()
    return total - world[x][y]

def new_state(world, x, y):
    neighbors = alive(world, x, y)
    if neighbors == 3:
        return 1
    elif neighbors == 2 and world[x, y] == 1:
        return 1
    else:
        return 0

def evolve(world):
    rows, cols = world.shape
    new_world = np.zeros(world.shape, dtype = int)
    for row in range(0, rows):
        for col in range(0, cols):
            new_world[row, col] = new_state(world, row, col)
    return new_world