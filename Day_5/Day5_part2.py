rules = {}
pages = []
mid = []

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
        elif len(line) > 0:
            numbers = [int(num.strip()) for num in line.split(",")]
            pages.append(numbers)



for pg in pages:

    position = {page: idx for idx, page in enumerate(pg)}
    valid = True
    
    for x, ys in rules.items():
        for y in ys:
            if x in position and y in position:
                if position[x] > position[y]:
                    valid = False

                    break
        if not valid: break
    
    if not valid:

        fixed = pg[:]
        n = len(fixed)

        switched = True

        while switched:
            switched = False
            for i in range(n - 1):
                a = fixed[i]
                b = fixed[i + 1]
                if a in rules.get(b,[]):
                    fixed[i], fixed[i+1] = fixed[i+1], fixed[i]
                    switched = True

        mid.append(fixed[len(fixed) // 2])
print(sum(mid))
