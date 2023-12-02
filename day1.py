# Day 1 Solution: Calibration Problem
# Txt file input

def calibration(str):
    # Large list of lines as input
    sum = 0
    for line in str.splitlines():
        num = calibration_helper(line)
        sum += int(num)
    return sum

def calibration_helper(str):
    # Get first and last number in string
    fnum, lnum = 0, 0
    for i in str:
        if i.isdigit():
            fnum = int(i)
            break
    for i in reversed(str):
        if i.isdigit():
            lnum = int(i)
            if fnum == lnum:
                print("Sum" + i + i)
                print("Found" + i)
                return i + i
            break
    print(str(fnum) + str(lnum))
    return fnum + lnum

input = open("input.txt").read()
print(calibration(input))