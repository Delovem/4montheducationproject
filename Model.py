from sqlalchemy import create_engine


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class Product():
    '''Класс определяющий товары'''
    def __init__(self, name='', price=0, count=0):
        '''инициализация класса'''
        self.name = name
        self.price = price
        self.count = count

    def product_info(self):
        '''вывод информации о продукте'''
        print(f'name = {self.name}, price = {self.price}$, count = {self.count}')

    def add_product(self):
        '''добавление товара в список'''
        pass
    def delete_product(self):
        '''удаление товара из списка'''
        pass

    def minprice(self):
        '''возвращает товар с минимальной ценой'''
        pass

    def maxprice(self):
        '''возвращает товар с максимальцой ценой'''
        pass


#БД




#Импорт файла





if __name__ == "__main__":
    Velociped = Product("Велосипед", 500, 4)
    Cow = Product("Корова", 3000, 6)

print(Cow.product_info())