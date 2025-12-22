with open('aoc4.txt', 'r') as f:
    grid = [line.strip() for line in f]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

count = 0
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
                count += 1

print(count)
