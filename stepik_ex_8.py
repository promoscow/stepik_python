students = dict()
for i in range(11):
    students[i + 1] = []

with open('dataset_3380_5.txt', encoding='utf8') as inf:
    for line in inf:
        student_data = line.split('\t')
        students[int(student_data[0])].append(int(student_data[2]))

for k, v in students.items():
    if len(v) == 0:
        print(k, '-')
    else:
        result = 0
        for i in v:
            result += i
        result = result / len(v)
        print(k, result)
