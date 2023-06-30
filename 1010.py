def factorial(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = factorial(M) // (factorial(M -N) * factorial(N))
    print(ans)