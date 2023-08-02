N = int(input())
condo = []
for _ in range(N):
    D, C = map(int, input().split())
    condo.append([D, C])
condo.sort()
cost = 10001
cnt = 0
for i in condo:
    temp = i[1]
    if temp < cost:
        cost = temp
        cnt += 1
print(cnt)