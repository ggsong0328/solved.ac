import sys
width, length = map(int, sys.stdin.readline().split())
w_lst = [0, width]
l_lst = [0, length]

N = int(sys.stdin.readline())

for _ in range(N):
    t, n = map(int, sys.stdin.readline().split())
    if t == 0:
        l_lst.append(n)
    else:
        w_lst.append(n)
l_lst.sort()
w_lst.sort()

l_max = 0
for i in range(1, len(l_lst)):
    l_max = max(l_max, l_lst[i] - l_lst[i-1])

w_max = 0
for i in range(1, len(w_lst)):
    w_max = max(w_max, w_lst[i] - w_lst[i-1])

print(w_max * l_max)