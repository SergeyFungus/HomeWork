def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(b = 25)
print_params(c = [1,2,3])
values_list = [15, 17.5, 'строка1']
values_dict = {'a': 17, 'b': 15.5, 'c': 'строка2'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['строка3', False]
print_params(*values_list_2, 42)
