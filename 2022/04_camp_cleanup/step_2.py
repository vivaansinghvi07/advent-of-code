print(sum([bool({*range(a, b+1)}&{*range(x, y+1)}) for [(a, b), (x, y)] in map(lambda x: list(map(lambda y: tuple(map(int, y.split('-'))), x.split(','))), [*open("input.txt")])]))