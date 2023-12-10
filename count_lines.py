import os
def disp_year(y: str):
    dirs = sorted([d for d in os.listdir(y) if d[:2].isnumeric()], key=lambda x: int(x[:2]))
    files, n, t = [sorted([f for f in os.listdir(f"{y}/{d}") if f != "input.txt"]) for d in dirs], '\n', '    '
    return n.join([f"{y}:"] + [f"{d}:{n}{n.join([t+''.join(f.split('.')[:-1]) + ': ' + str(len([*open(f'{y}/{d}/{f}')])) for f in fs])}" for d, fs in zip(dirs, files)])
print("\n\n".join([disp_year(y) for y in ["2022", "2023"]]))
