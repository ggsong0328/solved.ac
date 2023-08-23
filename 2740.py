import sys

N, M = map(int, sys.stdin.readline().split())
A = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    A.append(row)

M, K = map(int, sys.stdin.readline().split())
B = []
for i in range(M):
    row = list(map(int, sys.stdin.readline().split()))
    B.append(row)

result = []
for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        dp = 0
        for k in range(len(B)):
            dp += A[i][k] * B[k][j]
        row.append(dp)
    result.append(row)

for row in result:
    print(*row)