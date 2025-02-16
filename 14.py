queens = []
for i in range(8):
    x, y = map(int, input(f"{i+1} ферзь: ").split())
    queens.append((x, y))

attacking = False

for i in range(8):
    for j in range(i + 1, 8):
        x1, y1 = queens[i]
        x2, y2 = queens[j]
        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            attacking = True
            break
    if attacking:
        break

if attacking:
    print("YES")
else:
    print("NO")
