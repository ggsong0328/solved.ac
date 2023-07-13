N = int(input())
K = int(input())

prime = [True] * (N + 1)
for i in range(2, N+1):
    if prime[i]:
        for j in range(2 * i, N + 1, i):
            prime[j] = False

num = [1] * (N + 1)
for i in range(2, N + 1):
    if prime[i] and i > K:
        for j in range(i, N + 1, i):
            num[j] = 0    
print(sum(num) - 1)