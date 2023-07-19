N = int(input())

pan = [['.' for j in range(N)] for i in range(N)]

move = list(input().rstrip())
#print(move)

idx = 0
current_idx = [0, 0]
while idx != len(move):
    if move[idx] == 'D':
        if current_idx[0] + 1 >= N:
            pass
        else:
            if pan[current_idx[0]][current_idx[1]] == '+':
                pass
            elif pan[current_idx[0]][current_idx[1]] == '-':
                pan[current_idx[0]][current_idx[1]] = '+'
            else:
                pan[current_idx[0]][current_idx[1]] = '|'
            current_idx[0] += 1
            if pan[current_idx[0]][current_idx[1]] == '+':
                pass
            elif pan[current_idx[0]][current_idx[1]] == '-':
                pan[current_idx[0]][current_idx[1]] = '+'
            else:
                pan[current_idx[0]][current_idx[1]] = '|'
    elif move[idx] == 'U':
        if current_idx[0] - 1 < 0:
            pass
        else:
            if pan[current_idx[0]][current_idx[1]] == '+':
                pass
            elif pan[current_idx[0]][current_idx[1]] == '-':
                pan[current_idx[0]][current_idx[1]] = '+'
            else:
                pan[current_idx[0]][current_idx[1]] = '|'
            current_idx[0] -= 1
            if pan[current_idx[0]][current_idx[1]] == '+':
                pass
            elif pan[current_idx[0]][current_idx[1]] == '-':
                pan[current_idx[0]][current_idx[1]] = '+'
            else:
                pan[current_idx[0]][current_idx[1]] = '|'
    elif move[idx] == 'R':
        if current_idx[1] + 1 >= N:
            pass
        else:
            if pan[current_idx[0]][current_idx[1]] == '+':
                pass
            elif pan[current_idx[0]][current_idx[1]] == '|':
                pan[current_idx[0]][current_idx[1]] = '+'
            else:
                pan[current_idx[0]][current_idx[1]] = '-'
            current_idx[1] += 1
            if pan[current_idx[0]][current_idx[1]] == '+':
                pass
            elif pan[current_idx[0]][current_idx[1]] == '|':
                pan[current_idx[0]][current_idx[1]] = '+'
            else:
                pan[current_idx[0]][current_idx[1]] = '-'
    elif move[idx] == 'L':
        if current_idx[1] - 1 < 0:
            pass
        else:
            if pan[current_idx[0]][current_idx[1]] == '+':
                pass
            elif pan[current_idx[0]][current_idx[1]] == '|':
                pan[current_idx[0]][current_idx[1]] = '+'
            else:
                pan[current_idx[0]][current_idx[1]] = '-'
            current_idx[1] -= 1
            if pan[current_idx[0]][current_idx[1]] == '+':
                pass
            if pan[current_idx[0]][current_idx[1]] == '|':
                pan[current_idx[0]][current_idx[1]] = '+'
            else:
                pan[current_idx[0]][current_idx[1]] = '-'
    
    idx += 1

for i in range(N):
    print(*pan[i],sep='')