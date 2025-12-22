
K = 12


def max_subsequence_of_length(s: str, k: int) -> str:
    s = s.strip()
    n = len(s)
    if n <= k:
        return s
    drop = n - k
    stack: list[str] = []
    for ch in s:
        while drop and stack and stack[-1] < ch:
            stack.pop()
            drop -= 1
        stack.append(ch)
    return ''.join(stack[:k])


def main() -> None:
    total = 0
    with open('aoc3.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            best = max_subsequence_of_length(line, K)
            total += int(best)
    print(total)


if __name__ == '__main__':
    main()
