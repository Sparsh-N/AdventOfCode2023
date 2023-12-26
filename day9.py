# Day 9: Mirage Maintenance

def extrapolate(array):
    changes = []

    for i in range(len(array) - 1):
        curr = array[i]
        next = array[i + 1]
        difference = next - curr
        changes.append(difference)

    if all(element == 0 for element in array):
        return 0

    diff = extrapolate(changes)
    return array[-1] + diff

total = 0

with open("input.txt", "r") as file:
    for line in file:
        # Read the numbers as a list
        nums = list(map(int, line.split()))
        # Call the recursive extrapolate func, sum them together for eachline
        total += extrapolate(nums)

print(total)
