def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(str_number[1:])
    else:
        return first


result = get_multiplied_digits(40203) # Функция возвращает 0 в данном случае т.к. требовалось
print(result)                         # вычислить произведение всех цифр числа, а 0 тоже
result = get_multiplied_digits(41213)
print(result)