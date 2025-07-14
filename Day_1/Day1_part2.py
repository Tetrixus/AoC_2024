import sys

left_column = []
right_column = []
similarity = []

with open("puzzle_input.txt") as file:
  for line in file:
    
    x = (line[:6])
    left_column.append(int(x))

    x = (line[8:13])
    right_column.append(int(x))

for position in left_column:
  count = right_column.count(position)
  similarity.append(position*count)

print(sum(similarity))