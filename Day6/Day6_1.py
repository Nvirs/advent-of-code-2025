with open('day6.txt', 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]


width = len(lines[0])


separators = []
for col in range(width):
    if all(line[col] == ' ' for line in lines):
        separators.append(col)


problems = []
prev = 0
for sep in separators:
    if sep > prev:
        problems.append((prev, sep))
    prev = sep + 1
if prev < width:
    problems.append((prev, width))

total = 0
for start, end in problems:
    numbers = []
    for row in range(4):
        row_str = lines[row][start:end]
        nums = [int(x) for x in row_str.split() if x.strip()]
        numbers.extend(nums)
    op_str = lines[4][start:end]
    op = op_str.replace(' ', '')
    if op == '*':
        result = 1
        for n in numbers:
            result *= n
    elif op == '+':
        result = sum(numbers)
    
    
    total += result

print(total)
