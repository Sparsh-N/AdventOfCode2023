# Day 6 Wait times and races?
# My logic/intuition: 
# Parse input -> Recieve both inputs as dicts, one for time other for distance
# Create a function to count all the times you can win given time and distance. loop to check if dist is less than
# the computed time and increment if value of i is more than it. Loop until end of times.
# Append the count and multiply the results with each other.

with open("input.txt") as inp:
    lines = inp.read().strip().split("\n")

times = list(map(int, lines[0].split()[1:]))
dists = list(map(int, lines[1].split()[1:]))

def ways(c, t, d):
    for i in range(t):
        if d < i * (t - i):
            c += 1
    return c

# List of count of answers, no need to hold individual permutations.
perm = 1

for i in range(len(times)):
    perm *= ways(0, times[i], dists[i])

print(perm)