def main():
    total = 0
    with open('aoc3.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            digits = [int(c) for c in line]
            n = len(digits)
            max_jolt = 0
            for i in range(n):
                for j in range(i+1, n):
                    jolt = 10 * digits[i] + digits[j]
                    if jolt > max_jolt:
                        max_jolt = jolt
            total += max_jolt
    print(total)

if __name__ == '__main__':
    main()
