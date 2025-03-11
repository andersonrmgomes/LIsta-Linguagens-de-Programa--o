import sys

def solve():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    points.sort()

    dp = {}
    max_len = 0

    for x, y in points:
        dp[(x, y)] = 1
        for px, py in dp:
            if px < x and abs(y - py) == 2:
                dp[(x, y)] = max(dp[(x, y)], dp[(px, py)] + 1)
        max_len = max(max_len, dp[(x, y)])

    return max_len

while True:
    try:
        print(solve())
    except EOFError:
        break