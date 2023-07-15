N, M = map(int, input().split())
pic = [[0 for j in range(100)] for i in range(100)]
for _ in range(N):
    l_x, l_y, r_x, r_y = map(int, input().split())
    for i in range(l_x-1, r_x):
        for j in range(l_y-1, r_y):
            pic[i][j] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if pic[i][j] > M:
            cnt += 1
print(cnt)