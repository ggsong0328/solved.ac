N = int(input())
mine = [list(input().rstrip()) for _ in range(N)]
map = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        cnt = 0
        if mine[i][j] != '.':
            map[i][j] = '*'
        else:
            if i - 1 >= 0:
                if mine[i-1][j] != '.':
                    cnt += int(mine[i-1][j])
                if j - 1 >= 0:
                    if mine[i-1][j-1] != '.':
                        cnt += int(mine[i-1][j-1])
                if j + 1 <= N - 1:
                    if mine[i-1][j+1] != '.':
                        cnt += int(mine[i-1][j+1])
            if i + 1 <= N - 1:
                if mine[i+1][j] != '.':
                    cnt += int(mine[i+1][j])
                if j - 1 >= 0:
                    if mine[i+1][j-1] != '.':
                        cnt += int(mine[i+1][j-1])
                if j + 1 <= N - 1:
                    if mine[i+1][j+1] != '.':
                        cnt += int(mine[i+1][j+1])
            if j - 1 >= 0:
                if mine[i][j-1] != '.':
                    cnt += int(mine[i][j-1])
            if j + 1 <= N - 1:
                if mine[i][j+1] != '.':
                    cnt += int(mine[i][j+1])
            
            if cnt >= 10:
                map[i][j] = "M"
            else:
                map[i][j] = cnt
            
for i in range(N):
    for j in range(N):
        print(map[i][j], end='')
    print()

            
                

            