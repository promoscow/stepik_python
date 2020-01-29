n = int(input())

if n == 1:
    print(n)
else:
    direction = 'left'
    result = [[0 for j in range(n)] for u in range(n)]
    x = 0
    y = 0
    count_in_line = 0
    max_count_in_line = n
    for i in range(n * n + 1):
        if i == 0:
            continue
        count_in_line += 1
        result[y][x] = i
        if direction.__eq__('left'):
            if count_in_line % max_count_in_line == 0 or (x < n and result[y][x + 1] != 0):
                direction = 'down'
                count_in_line = 1
            else:
                x += 1
        if direction.__eq__('down'):
            if count_in_line % max_count_in_line == 0 or (y < n and result[y + 1][x] != 0):
                direction = 'right'
                count_in_line = 1
            else:
                y += 1
        if direction.__eq__('right'):
            if count_in_line % max_count_in_line == 0 or (x > 0 and result[y][x - 1] != 0):
                direction = 'up'
                count_in_line = 1
                max_count_in_line -= 1
            else:
                x -= 1
        if direction.__eq__('up'):
            if count_in_line % max_count_in_line == 0 or (y > 0 and result[y - 1][x] != 0):
                direction = 'left'
                count_in_line = 1
                x += 1
            else:
                y -= 1
    for i in result:
        for j in i:
            print(j, end=' ')
        print()