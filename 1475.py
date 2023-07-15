N = input()
room = [0] * 10
for i in range(len(N)):
    idx = int(N[i])
    if idx == 6 or idx == 9:
        if room[6] <= room[9]:
            room[6] += 1
        else:
            room[9] += 1
    else:
        room[idx] += 1

print(max(room))