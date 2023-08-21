import sys

plane = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for row in range(x1, x2):
        for col in range(y1, y2):
            plane[row][col] = 1

ans = 0

for i in plane:
    ans += i.count(1)

print(ans)