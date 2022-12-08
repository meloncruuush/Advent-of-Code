def parse(filename):
    with open(filename) as f:
        data = [l.strip().split(" ") for l in f.readlines()]
        fs = {}
        upper = []
        current = fs
        for c in data:
            if c[0] == "$":
                if c[1] == "cd":
                    if c[2] == "/":
                        current = fs
                        upper = []
                    elif c[2] == "..":
                        current = upper.pop()
                    else:
                        upper.append(current)
                        current = current[c[2]]
            else:
                if c[0] == "dir":
                    newdir = {}
                    current[c[1]] = newdir
                else:
                    current[c[1]] = int(c[0])
        return fs


def size(d, dirsize=None):
    # file
    if type(d) == int:
        return d
    # directory (recursive)
    s = 0
    for o in d:
        s += size(d[o], dirsize)
    if dirsize != None:
        dirsize.append(s)
    return s


def part1(filename):
    fs = parse(filename)
    dirsize = []
    _ = size(fs, dirsize)
    return sum([s for s in dirsize if s < 100000])


def part2(filename):
    fs = parse(filename)
    dirsize = []
    tot = size(fs, dirsize)
    space = 70000000
    needed = 30000000
    for s in sorted(dirsize):
        if space-tot+s > needed:
            return s


print("Part 1:", part1("Day07/input.txt"))
print("Part 2:", part2("Day07/input.txt"))
