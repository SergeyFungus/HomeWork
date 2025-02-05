def is_prime(func):
    def is_prime_sum_tree(*args, **kwargs):
        result = func(*args, **kwargs)
        flag = True
        for i in range(2, (result // 2) + 1):
            if result % i == 0:
                flag = False
                break
        if flag:
            print('Простое')
        else:
            print('Составное')
        return result
    return is_prime_sum_tree


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
