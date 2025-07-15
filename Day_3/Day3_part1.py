import re

mem = []
total = 0

with open("puzzle_input.txt") as file:
    memory = file.read()
    mem = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)
    for x, y in mem:
        total += int(x) * int(y)
    print(total)