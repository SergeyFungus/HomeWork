from itertools import product


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{str(self.name)}, {str(self.weight)}, {str(self.category)}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        product = file.read()
        file.close()
        return product

    def add(self, *products):
        s = self.get_products()
        file = open(self.__file_name, 'w')
        for i in products:
            # print(s.find(str(i)))
            flag = True
            for j in s.split('\n'):
                if i.name == j.split(', ')[0] and i.category == j.split(', ')[2]:
                    i.weight += float(j.split(', ')[1])
                    s = s.replace(j, str(i))
                    print(f'Продукт {i.name} уже был в магазине, его общий вес теперь равен {i.weight}')
                    flag = False
            if flag:
                s += f'{str(i)}\n'
        file.write(s)
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())


















