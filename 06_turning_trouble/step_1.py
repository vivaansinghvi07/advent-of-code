print(min([i + 4 for (i, c) in enumerate(zip([*open("input.txt")][0], [*open("input.txt")][0][1:], [*open("input.txt")][0][2:], [*open("input.txt")][0][3:])) if len(set(c)) == 4]))