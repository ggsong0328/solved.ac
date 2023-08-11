import sys
cp = int(sys.stdin.readline())
location = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(cp):
	x, y = list(map(int, sys.stdin.readline().split()))
	
	for row in range(x, x + 10):
		for col in range(y, y + 10):
			location[row][col] = 1
			
ans = 0

for i in location:
	ans += i.count(1)
	
print(ans)
	