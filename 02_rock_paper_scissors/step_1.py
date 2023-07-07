print(sum([0, 3, 6][o-s+1] + o for s, o in map(lambda x: map(lambda c: ['A', 'B', 'C', 'X', 'Y', 'Z'].index(c) % 3 + 1, x.split()), open("input.txt"))))
