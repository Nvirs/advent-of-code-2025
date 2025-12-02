with open('aoc2.txt', 'r') as f:
    line = f.read().strip()

ranges = line.split(',')
total = 0

def is_invalid(s):
    for r in range(1, len(s) // 2 + 1):
        if len(s) % r == 0:
            part = s[:r]
            if all(s[i*r:(i+1)*r] == part for i in range(len(s) // r)):
                return True
    return False

for r in ranges:
    start, end = map(int, r.split('-'))
    for id in range(start, end + 1):
        s = str(id)
        if is_invalid(s):
            total += id

print(total)
