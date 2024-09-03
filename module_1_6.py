my_dict ={'Denis':2000, 'Anton':1998, 'Sergey':2001}
print(my_dict)
print(my_dict['Sergey'])
print(my_dict.get('Max','Такого имени нет'))
my_dict.update({'Slavik':2002, 'Andrey':2000})
print(my_dict.pop('Anton'))
print(my_dict)

my_set = {1, 2, 3, 2, 3, 'Str', 'Ignat', 'Str'}
print(my_set)
my_set.add(5)
my_set.add(4)
print(my_set)
my_set.discard(4)
print(my_set)
