safe = []

with open("puzzle_input.txt") as file:
  for line in file:

    nums = [int(n) for n in line.strip().split()]

    inc = all(nums[i + 1] > nums[i] and nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1))
    dec = all(nums[i + 1] < nums[i] and nums[i] - nums[i + 1] <= 3 for i in range(len(nums) - 1))

    if inc or dec:
      safe.append(nums)
    
    else:
      for i in range(len(nums)):
        
        temp = nums[:i] + nums[i+1:]\

        inc = all(temp[i + 1] > temp[i] and temp[i + 1] - temp[i] <= 3 for i in range(len(temp) - 1))
        dec = all(temp[i + 1] < temp[i] and temp[i] - temp[i + 1] <= 3 for i in range(len(temp) - 1))

        if inc or dec:
          safe.append(nums)
          break

print(len(safe))
