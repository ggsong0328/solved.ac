N = int(input())
room = [list(input().rstrip()) for _ in range(N)]

w_cnt = 0
l_cnt = 0
idx = 0



for i in range(N):
    cnt = 0
    for j in range(N):
        if room[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                w_cnt += 1
                cnt = 0
            else:
                cnt = 0
    if cnt >= 2:
        w_cnt += 1
        

for i in range(N):
    cnt = 0
    for j in range(N):
        if room[j][i] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                l_cnt += 1
                cnt = 0
            else:
                cnt = 0
    if cnt >= 2:
        l_cnt += 1

print(w_cnt, l_cnt)

