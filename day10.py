# Day 10 : Pipe Maze (BFS was fun to remember, shout out to my data structures prof.)
from collections import deque

with open("input.txt", "r") as file:
    maze = [line.strip() for line in file]
neighbors = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}

# Find starting position
start_x, start_y = next((xi, yi) for yi, line in enumerate(maze) for xi, c in enumerate(line) if c == "S")
queue = deque()
# Check neighbors
for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    neighbor_char = maze[start_y + dy][start_x + dx]
    if neighbor_char in neighbors:
        for dx2, dy2 in neighbors[neighbor_char]:
            if start_x == start_x + dx + dx2 and start_y == start_y + dy + dy2:
                queue.append((1, (start_x + dx, start_y + dy)))
dists = {(start_x, start_y): 0}
assert len(queue) == 2

# BFS (Thank you prof siek)
while queue:
    d, (x, y) = queue.popleft()

    if (x, y) in dists:
        continue

    dists[(x, y)] = d

    for dx, dy in neighbors[maze[y][x]]:
        queue.append((d + 1, (x + dx, y + dy)))

res = max(dists.value())
print(res)
