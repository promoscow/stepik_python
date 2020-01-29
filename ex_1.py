def f(xi):
    return xi * xi


n = int(input())

l = []
for i in range(n):
    l.append(int(input()))
d = dict()
m = dict()
counter = 0
for i in l:
    d[counter] = dict()
    if i not in m:
        d[counter][i] = f(i)
        m[i] = d[counter][i]
        counter += 1
    else:
        d[counter][i] = m[i]
        counter += 1
for v in d.values():
    for v1 in v.values():
        print(v1)
