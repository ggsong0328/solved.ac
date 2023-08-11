import sys
N = int(sys.stdin.readline())
nation_cnt = [0]*N
arr = []
for _ in range(N):
	arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: -x[2])

print(*arr[0][:2])
print(*arr[1][:2])

idx = 2

if arr[0][0] == arr[1][0]:
	while arr[0][0] == arr[idx][0]:
		idx += 1

print(*arr[idx][:2])
	