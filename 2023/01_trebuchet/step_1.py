print(sum(int(l[0] + l[-1]) for l in map(lambda x: [i for i in x if i.isdigit()], open("input.txt"))))
