def handle_diffs(l: list[int]) -> int: return 0 if not any(l) else l[-1] + handle_diffs([j-i for i,j in zip(l, l[1:])])
print(sum([handle_diffs(l) for l in map(lambda x: list(map(int, x.split())), open("input.txt"))]))
