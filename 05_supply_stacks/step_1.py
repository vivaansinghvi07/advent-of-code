stack, moves = (l:=''.join([*open("input.txt")]).split('\n\n'))[0].replace('[', '').replace(']', '').replace('    ', '  ').split('\n')[:-1], l[1]
stack = [[l for line in stack if (l:=line[i]) != ' '] for i in range(len(stack[0])) if i % 2 == 0]
for move in map(lambda x: list(map(int, x.replace('move ', '').replace('from ', '').replace('to ', '').split())), moves.split('\n')):
    stack[move[2]-1] = [*reversed(stack[move[1]-1][:move[0]])] + stack[move[2]-1]
    stack[move[1]-1][:move[0]] = []
print(*[line[0] for line in stack], sep='')