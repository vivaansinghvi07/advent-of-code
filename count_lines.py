import os
dirs = sorted([d for d in os.listdir(".") if d[:2].isnumeric()], key=lambda x: int(x[:2]))
files, n, t = [sorted([f for f in os.listdir(f"./{d}") if f != "input.txt"]) for d in dirs], '\n', '    '
print(n.join([f"{d}:{n}{n.join([t+''.join(f.split('.')[:-1]) + ': ' + str(len([*open(f'{d}/{f}')])) for f in fs])}" for d, fs in zip(dirs, files)]))