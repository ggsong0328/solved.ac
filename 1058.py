N = int(input())
friend = [list(input().strip()) for _ in range(N)]
check = [[0] * N for _ in range(N)]  # 올바르게 초기화

count = 0

for i in range(N):
    for j in range(N):
        if i == j or i > j:
            continue
        else:
            if friend[i][j] == 'Y':
                check[i][j] += 1
                check[j][i] += 1

for i in range(N):
    for j in range(N):
        if friend[i][j] == 'Y':
            for k in range(N):
                if friend[j][k] == 'Y' and i != k:
                    check[i][k] = 1

# 최댓값 찾기
max_sum = 0
for i in range(N):
    if max_sum < sum(check[i]):
        max_sum = sum(check[i])

print(max_sum)
