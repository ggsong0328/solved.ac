from sys import stdin

N, M, L, K = map(int, stdin.readline().split())
stars = [list(map(int, stdin.readline().split())) for _ in range(K)]

result = float('inf')

for x1, y1 in stars:
    for x2, y2 in stars:
        count = 0
        for x, y in stars:
            if x1 <= x <= x1 + L and y2 <= y <= y2 + L: #트럼펄린에 부딪히는 별똥별
                count += 1
        result = min(result, K - count)

print(result)
