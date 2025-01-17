first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x[0]) - len(x[1])) for x in zip(first, second) if len(x[0]) != len(x[1]))
# случай когда известно что списки равны
second_result_1 = (len(first[i]) == len(second[i]) for i in range(len(first)))
# общее решение
second_result_2 = (len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i == j )

print(list(first_result))
print(list(second_result_1))
print(list(second_result_2))