from sys import stdin

N, M = map(int, stdin.readline().split())
num = [list(stdin.readline()) for _ in range(N)]

max_len = min(N, M)
result = 1

for length in range(max_len, 0, -1):
    for i in range(N - length + 1):
        for j in range(M - length + 1):
            if num[i][j] == num[i][j + length - 1] == num[i + length - 1][j] == num[i + length - 1][j + length - 1]:
                result = max(result, length)

print(result ** 2)