map = {}
count = []


with open("puzzle_input.txt") as file:
    lines = [line.strip() for line in file]

    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            map [(r, c)] = char

for key, char in map.items():
    if char == "X":
        r, c = key
        #I understand this part may be shortened
        #but this is approach i figured out my self
        #and even if code looks like shit it does the job ok?
        #I'll (probly some day) try to find better solution
        temp_key = (r, c - 1)
        if temp_key in map and map[temp_key] == "M":
            temp_key = (r, c - 2)
            if temp_key in map and map[temp_key] == "A":
                temp_key = (r, c - 3)
                if temp_key in map and map[temp_key] == "S":
                    count.append(key)
        
        temp_key = (r, c + 1)
        if temp_key in map and map[temp_key] == "M":
            temp_key = (r, c + 2)
            if temp_key in map and map[temp_key] == "A":
                temp_key = (r, c + 3)
                if temp_key in map and map[temp_key] == "S":
                    count.append(key)
        
        temp_key = (r + 1, c)
        if temp_key in map and map[temp_key] == "M":
            temp_key = (r + 2, c)
            if temp_key in map and map[temp_key] == "A":
                temp_key = (r + 3, c)
                if temp_key in map and map[temp_key] == "S":
                    count.append(key)
        
        temp_key = (r - 1, c)
        if temp_key in map and map[temp_key] == "M":
            temp_key = (r - 2, c)
            if temp_key in map and map[temp_key] == "A":
                temp_key = (r - 3, c)
                if temp_key in map and map[temp_key] == "S":
                    count.append(key)
        
        temp_key = (r - 1, c - 1)
        if temp_key in map and map[temp_key] == "M":
            temp_key = (r - 2, c - 2)
            if temp_key in map and map[temp_key] == "A":
                temp_key = (r - 3, c - 3)
                if temp_key in map and map[temp_key] == "S":
                    count.append(key)
        
        temp_key = (r - 1, c + 1)
        if temp_key in map and map[temp_key] == "M":
            temp_key = (r - 2, c + 2)
            if temp_key in map and map[temp_key] == "A":
                temp_key = (r - 3, c + 3)
                if temp_key in map and map[temp_key] == "S":
                    count.append(key)
        
        temp_key = (r + 1, c + 1)
        if temp_key in map and map[temp_key] == "M":
            temp_key = (r + 2, c + 2)
            if temp_key in map and map[temp_key] == "A":
                temp_key = (r + 3, c + 3)
                if temp_key in map and map[temp_key] == "S":
                    count.append(key)
        
        temp_key = (r + 1, c - 1)
        if temp_key in map and map[temp_key] == "M":
            temp_key = (r + 2, c - 2)
            if temp_key in map and map[temp_key] == "A":
                temp_key = (r + 3, c - 3)
                if temp_key in map and map[temp_key] == "S":
                    count.append(key)


print(len(count))