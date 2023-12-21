# Day 5
# Note: This one definetly took me a long time to understand. Didnt think I'd see number lines again but oh well.

with open("input.txt") as f:
    data = f.read().strip().split("\n")

# Split all the seeds, start from i = 2 because it is the second line.
seeds = list(map(int, data[0].split()[1:]))
mappings, i = [], 2

while i < len(data):
    mappings.append([])
    # Go to next line to process
    i += 1
    while i < len(data) and not data[i] == "":
        # D is start of distribution
        # S is start of source
        # R is the length of the range
        # Increment i to move to next place
        d, s, r = map(int, data[i].split())
        # Add this to the map of all data (list)
        mappings[-1].append((d, s, r))
        i += 1
    i += 1

def transform(seed):
    n = seed
    for mapping in mappings:
        for d, s, r in mapping:
            # Check and make sure all d, s, and r in the map is whithin the range.
            # If its in the range from src start to src start and len of range, we transform it
            if s <= n < s + r:
                n = d + (n - s)
                break
    # Return the modified number, which is a sum 
    return n

# result is the smallest seed in all of the transformations
res = min([transform(seed) for seed in seeds])
print(res)
