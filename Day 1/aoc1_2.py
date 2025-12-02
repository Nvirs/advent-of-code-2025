with open('aof_1.txt', 'r') as f:
    rotations = f.readlines()

position = 50
count = 0

for rotation in rotations:
    rotation = rotation.strip()
    if not rotation:
        continue
    dir = rotation[0]
    dist = int(rotation[1:])
    for _ in range(dist):
        if dir == 'L':
            position = (position - 1) % 100
        elif dir == 'R':
            position = (position + 1) % 100
        if position == 0:
            count += 1

print(count)
