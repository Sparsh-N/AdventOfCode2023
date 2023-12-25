# Day 8: Haunted Wasteland

# Read first line as instructions, amd remainder as information/store in dict
map, step_ct, curr = {}, 0, "AAA"
with open("input.txt") as file:
    step, *info = file.read().splitlines()
    # Remove first line read because its a empty
    info = info[1:]
    for line in info:
        pos, targets = line.split(" = ")
        # Create the map for each of the ways for every posn (i.e. AAA : (BBB, CCC))
        map[pos] = targets[1:-1].split(", ")
        
while curr != "ZZZ":
    step_ct += 1
    if step[0] == "L":
        curr = map[curr][0]
    else:
        curr = map[curr][1]
    step = step[1:] + step[0]

print(step_ct)