print(sum([(x := lambda y: max([i[0] if i else 0 for i in y]))(r)*x(b)*x(g) for (r, g, b) in map(lambda x: zip(*[[[int(''.join(filter(lambda x: x.isdigit(), p))) for p in s.split(', ') if c in p] for c in ['red', 'green', 'blue']] for s in x.split(':')[1].split(';')]), open("input.txt"))]))
