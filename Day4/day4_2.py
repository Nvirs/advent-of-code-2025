with open('aoc4.txt', 'r') as f:
    grid = [list(line.strip()) for line in f]

rows = len(grid)
cols = len(grid[0])

total = 0
while True:
    to_remove = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                adj = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '@':
                            adj += 1
                if adj < 4:
                    to_remove.append((i, j))
    if not to_remove:
        break
    for i, j in to_remove:
        grid[i][j] = '.'
    total += len(to_remove)

print(total)
