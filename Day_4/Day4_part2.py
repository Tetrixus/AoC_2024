map = {}
count = 0

with open("puzzle_input.txt") as file:
    lines = [line.strip() for line in file]
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            map[(r, c)] = char

def get_diag1(r, c):
    return [map.get((r - 1, c - 1)), map.get((r + 1, c + 1))]

def get_diag2(r, c):
    return [map.get((r + 1, c - 1)), map.get((r - 1, c + 1))]

valid_pairs = {
    (("M", "S"), ("M", "S")),
    (("M", "S"), ("S", "M")),
    (("S", "M"), ("M", "S")),
    (("S", "M"), ("S", "M")),
}

for (r, c), char in map.items():
    if char !=  "A":
     continue

    d1 = get_diag1(r, c)
    d2 = get_diag2(r, c)

    if (tuple(d1), tuple(d2)) in valid_pairs:
        count += 1

print(count)