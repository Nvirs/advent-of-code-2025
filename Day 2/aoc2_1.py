with open('aoc2.txt', 'r') as f:
    line = f.read().strip()

ranges = line.split(',')
total = 0

for r in ranges:
    start, end = map(int, r.split('-'))
    for id in range(start, end + 1):
        s = str(id)
        if len(s) % 2 == 0:
            half = len(s) // 2
            if s[:half] == s[half:]:
                total += id

print(total)
