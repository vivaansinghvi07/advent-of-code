rocks = [*map(lambda x: [*map(int, x.split(','))], [*open("input.txt")])]
x, y, z = [max([rock[i] for rock in rocks]) + 2 for i in range(3)]
cubes = [[[0 for _ in range(z)] for _ in range(x)] for _ in range(y)]
for rock in rocks: cubes[rock[1]][rock[0]][rock[2]] = 1
m = (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1)
print(6*len(rocks) - sum([cubes[y+j][x+i][z+k] for (i, j, k) in m for (x, y, z) in rocks]))