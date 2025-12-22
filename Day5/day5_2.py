with open('aoc5.txt', 'r') as f:
    lines = f.read().splitlines()

blank_index = next(i for i, line in enumerate(lines) if line.strip() == '')

ranges_lines = lines[:blank_index]

ranges = []
for line in ranges_lines:
    start, end = map(int, line.split('-'))
    ranges.append((start, end))
ranges.sort()

merged = []
for start, end in ranges:
    if not merged or merged[-1][1] < start:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

total = 0
for start, end in merged:
    total += end - start + 1

print(total)
