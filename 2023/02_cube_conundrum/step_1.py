print(sum([int(id) for (id, r, g, b) in map(lambda x: (x.split(':')[0][5:], *zip(*[[[int(''.join(filter(lambda x: x.isdigit(), p))) for p in s.split(', ') if c in p] for c in ['red', 'green', 'blue']] for s in x.split(':')[1].split(';')])), open("input.txt")) if max((x := lambda y: [i[0] for i in y if i])(r)) < 13 and max(x(g)) < 14 and max(x(b)) < 15]))
