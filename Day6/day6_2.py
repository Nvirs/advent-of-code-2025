with open('day6.txt', 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]
    
max_len = max(len(line) for line in lines)
lines = [line + ' ' * (max_len - len(line)) for line in lines]

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
    for col in range(start, end):
        digits = []
        for row in range(4):
            c = lines[row][col]
            if c != ' ':
                digits.append(c)
        if digits:
            num = int(''.join(digits))
            numbers.append(num)
    op_str = ''
    for col in range(start, end):
        c = lines[4][col]
        if c != ' ':
            op_str += c
    op = op_str
    
   
    if op == '*':
        result = 1
        for n in numbers:
            result *= n
    elif op == '+':
        result = sum(numbers)
    
    total += result

print(total)
