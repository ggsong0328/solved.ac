from sys import stdin

N, M = map(int, stdin.readline().split())
board = [list(stdin.readline()) for _ in range(N)]

def chess_board(board, x, y):
    count = [0, 0]
    colors = ['W', 'B']
    for i in range(x, x + 8):
        for j in range(y, y + 8): 
            if board[i][j] != colors[(i+j)%2]: #첫번째 칸이 W인 경우 - 행과 열의 합이 짝수인 칸의 색깔이 'W'여야한다
                count[0] += 1
            if board[i][j] != colors[(i+j+1)%2]: #첫번째 칸이 B인 경우 - 행과 열의 합이 짝수인 칸의 색깔이 'B'여야한다
                count[1] += 1
    return min(count)

result = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        result = min(result, chess_board(board, i, j))

print(result)
