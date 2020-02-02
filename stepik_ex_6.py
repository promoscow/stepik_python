checking_words = []
for i in range(int(input())):
    checking_words.append(input().lower())

words = set()
for i in range(int(input())):
    for j in input().split():
        words.add(j.lower())

for i in words:
    if i not in checking_words:
        print(i)
