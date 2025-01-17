def personal_sum(number):
    incorrect_data = 0
    result = 0
    for i in number:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {i}")
    return (result, incorrect_data)

def calculate_average(number):
    try:
        res_f1 = personal_sum(number)
        result = res_f1[0] / (len(number) - res_f1[1])
    except ZeroDivisionError:
        result = 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        result = None
    return result

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
