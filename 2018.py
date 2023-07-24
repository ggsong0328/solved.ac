N = int(input())

cnt = 0
sum = 0
end = 0

for start in range(N):
    while sum < N and end < N :
        sum += end + 1
        end += 1
    if sum == N:
        cnt += 1
    sum -= start + 1

print(cnt)