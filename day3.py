# Day 3: Gear Ratios

with open("input.txt") as f:
    schematic = f.read()

def valid_symbol(char):
    return char in "*+#$!@%&^+-=/"

def find_part_numsum(schema):
    lines = schema.strip().split('\n')
    # for line in lines:
    #     print(line)
    rows, cols = len(lines), len(lines[0])
    part_sum = 0

    for i in range(rows):
        for j in range(cols):
            if lines[i][j].isdigit():
                current_number = int(lines[i][j])
                found_symbol = False

                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < rows and 0 <= y < cols and valid_symbol(lines[x][y]):
                            found_symbol = True
                            break

                if found_symbol:
                    while j + 1 < cols and lines[i][j + 1].isdigit():
                        current_number = current_number * 10 + int(lines[i][j + 1])
                        j += 1
                    
                    part_sum += current_number

    return part_sum

print(find_part_numsum(schematic))