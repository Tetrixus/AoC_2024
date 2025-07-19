map = {}
count = 0

with open("puzzle_input.txt") as file:
    lines = [line.strip() for line in file]
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            map[(r, c)] = char

directions = {
    (0,1),
    (0,-1),
    (1,0),
    (-1,0),
    (1,1),
    (1,-1),
    (-1,1),
    (-1,-1)
}

for (r, c),  char in map.items():
    if char != "X":
        continue

    for dr, dc in directions:
        pos_1 = (r + dr, c + dc)
        pos_2 = (r + dr * 2, c + dc * 2)
        pos_3 = (r + dr * 3, c + dc * 3)

        if (
            map.get(pos_1) == "M" and
            map.get(pos_2) == "A" and
            map.get(pos_3) == "S"
        ):
            count += 1
print(count)
        