rules = {}
pages = []

with open("puzzle_input.txt") as file:
    for line in file:
        line = line.strip()
        if "|" in line:
            x, y = line.split("|")
            key = int(x)
            value = int(y)
            if key not in rules:
                rules[key] = []
            rules[key].append(value)
        elif len(line) > 1:
            numbers = [int(num.strip()) for num in line.split(",")]
            pages.append(numbers)

mid = []

for pg in pages:
    position = {page: idx for idx, page in enumerate(pg)}
    valid = True
    for x, ys in rules.items():
        for y in ys:
            if x in position and y in position:
                if position[x] >= position[y]:
                    valid = False
                    break
        if not valid:
            break
    if valid:
        mid_index = len(pg) // 2
        mid.append(pg[mid_index])

print(sum(mid))
