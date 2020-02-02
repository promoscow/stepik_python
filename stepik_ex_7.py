x = 0
y = 0
for i in range(int(input())):
    direction, distance = input().split()
    if direction == 'север':
        y += int(distance)
    if direction == 'юг':
        y -= int(distance)
    if direction == 'запад':
        x -= int(distance)
    if direction == 'восток':
        x += int(distance)
print(x, y)
