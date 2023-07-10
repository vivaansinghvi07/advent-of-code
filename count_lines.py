import os
dirs = sorted([d for d in os.listdir(".") if d[:2].isnumeric()], key=lambda x: int(x[:2]))
files = [[f for f in os.listdir(f"./{d}") if f != "input.txt"] for d in dirs]
for (d, fs) in zip(dirs, files):
    print(f"{d}:")
    for f in fs:
        print(f"\t{''.join(f.split('.')[:-1])}: {len([*open(f'{d}/{f}')])}")