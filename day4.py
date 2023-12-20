# Day 4: Scratchcard
t = 0

for line in open("input.txt"):
    # Remove the text before the :
    line = line.split(":")[1].strip()
    # Create 2 hashmaps, 1 for the stuff before line split and one after
    a, b = [list(map(int, k.split())) for k in line.split(" | ")]
    # Sum up each value for its corresponding number, do this for the entire set of a in set of b
    j = sum(q in a for q in b)
    # If its greater than 0, set the total to 2^sum-1 (-1 to account for a case of first index. It should double each time so its 2^e)
    if j > 0:
        t += 2 ** (j - 1)

print(t)