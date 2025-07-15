safe = []

with open("puzzle_input.txt") as file:
  for line in file:
    nums = [int(n) for n in line.strip().split()]

    increasing = all(nums[i + 1] > nums[i] and nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1))
    decreasing = all(nums[i + 1] < nums[i] and nums[i] - nums[i + 1] <= 3 for i in range(len(nums) - 1))

    if increasing or decreasing:
      safe.append(nums)
    
print(len(safe))
