def calculate_structure_sum(*args):
    if len(args) == 1:
        if isinstance(args[0], int) or isinstance(args[0], float):
            return args[0]
        if isinstance(args[0], str):
            return len(args[0])
        if isinstance(args[0], list) or isinstance(args[0], tuple) or isinstance(args[0], set):
            sum = 0
            for i in args[0]:
                sum += calculate_structure_sum(i)
            return sum
        if isinstance(args[0], dict) and args[0].__len__() == 0:
            return 0
        if isinstance(args[0], dict):
            sum = 0
            for i in args[0]:
                sum += calculate_structure_sum(i)
                sum += calculate_structure_sum(args[0].get(i))
            return sum

    if len(args) == 0:
        return 0
    sum = 0
    for i in args:
        sum += calculate_structure_sum(i)

    print(type(args))
    return 'ERROR'




data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
