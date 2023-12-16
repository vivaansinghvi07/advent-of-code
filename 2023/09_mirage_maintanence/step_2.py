print(sum([(f := lambda x: 0 if not any(x) else x[0] - f([j-i for i, j in zip(x, x[1:])]))(l) for l in map(lambda x: list(map(int, x.split())), open("input.txt"))]))
