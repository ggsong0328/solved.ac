def check_knight_move(before, after):
    if abs(ord(after[0]) - ord(before[0])) == 1:
        if abs(ord(after[1]) - ord(before[1])) == 2:
            return True
        else:
            return False
    elif abs(ord(after[0]) - ord(before[0])) == 2:
        if abs(ord(after[1]) - ord(before[1])) == 1:
            return True
        else:
            return False
    else: return False

knight = []
check_move = []
check_dup = True
for i in range (36):
    move = input()
    knight.append(move)
for k in range(len(knight)-1):
    if check_knight_move(knight[k], knight[k+1]) == False:
        check_move.append(0)
    else:
        check_move.append(1)
        
if len(knight) != len(set(knight)):
    check_dup = False

if (check_dup == False) or (0 in check_move) or (check_knight_move(knight[-1], knight[0]) == False):
    print("Invalid")
else:
    print("Valid")
