import re

mem = []
total = 0
enabled = True

with open("puzzle_input.txt") as file:
    memory = file.read()

    chunks = re.split(r"(do\(\)|don't\(\))", memory)

    for chunk in chunks:
        if chunk == "do()":
            enabled = True
        elif chunk == "don't()":
            enabled = False
        elif enabled:
        
            mem  = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", chunk)
            for x, y in mem:
                total += int(x) * int(y)

    print(total)