with open('aoc5.txt', 'r') as f:
    lines = f.read().splitlines()


blank_index = next(i for i, line in enumerate(lines) if line.strip() == '')

ranges_lines = lines[:blank_index]
ids_lines = lines[blank_index + 1:]


ranges = []
for line in ranges_lines:
    start, end = map(int, line.split('-'))
    ranges.append((start, end))


ids = [int(line) for line in ids_lines]


count = 0
for id in ids:
    if any(start <= id <= end for start, end in ranges):
        count += 1

print(count)
