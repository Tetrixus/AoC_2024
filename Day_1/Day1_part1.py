left_column = []
right_column = []

with open("puzzle_input.txt") as file:
  for line in file:
    
    x = (line[:6])
    left_column.append(int(x))

    x = (line[8:13])
    right_column.append(int(x))

sorted_left = sorted(left_column)
sorted_right = sorted(right_column)

distances = [abs(a - b) for a, b in zip(sorted_left, sorted_right)] 

total_distance = sum(distances)

print(total_distance)