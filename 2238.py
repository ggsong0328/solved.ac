U, N = map(int, input().split())
name = [[] for _ in range(10001)]
bet = [0 for _ in range(10001)]
low = 10001
for _ in range(N):
    n, b = input().split()
    b = int(b)
    name[b].append(n)
    bet[b] += 1
for i in range(10001):
    if bet[i] != 0:
        low = min(bet[i], low)
for i in range(10001):
    if low == bet[i]:
        print(name[i][0], i)
        break

