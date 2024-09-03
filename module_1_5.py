immutable_var = (1, 'Hay', 2.5)
print(immutable_var)
#immutable_var[0] = 0  данную операцию нельзя выполнить т.к. кортеж неизменяемый контейнер
mutable_list = [1, 'Hay', 2.5]
mutable_list[0] = 2
print(mutable_list)