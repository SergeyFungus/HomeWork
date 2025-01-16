def add_everything_up(a, b):
    try:
        d = round(a + b, 3)
    except TypeError:
        d = str(a) + str(b)
    return d

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


