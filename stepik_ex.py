import sys

s = ''
for i in range(len(sys.argv)):
    if i > 0:
        s += sys.argv[i]
        s += ' '
print(s.strip())

