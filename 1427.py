num = []
N = int(input())
while N // 10 != 0:
    num.append(N % 10)
    N = N // 10
num.append(N)
num.sort(reverse=True)
ans = list(map(str, num))
print(''.join(ans))
