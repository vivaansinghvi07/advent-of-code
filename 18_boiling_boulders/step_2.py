rocks,q,b = [*map(lambda x: [*map(int, x.split(','))], [*open("input.txt")])],[(0,0,0)],[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,-1),(0,0,1)]
for [x, y, z] in [[max([rock[i] for rock in rocks]) + 2 for i in range(3)]]: xx,yy,zz,cubes = x,y,z,[[[0 for _ in range(z)] for _ in range(x)] for _ in range(y)]
for rock in rocks: cubes[rock[1]][rock[0]][rock[2]] = 1
while len(q)>0:
    cubes[(c:=q.pop())[0]][c[1]][c[2]] = -1
    q.extend([*filter(lambda z: cubes[z[0]][z[1]][z[2]] == 0, filter(lambda j: all([0<=i<k for i,k in zip(j, [yy,xx,zz])]), map(lambda x: (x[0]+c[0], x[1]+c[1], x[2]+c[2]), b)))])
print(6*len(rocks)-sum([max(cubes[y+j][x+i][z+k], 0)for(i,j,k)in b for(x,y,z)in rocks])-sum([cubes[y+j][x+i][z+k] for (i,j,k) in b for y in range(yy) for x in range(xx) for z in range(zz) if cubes[y][x][z] == 0]))