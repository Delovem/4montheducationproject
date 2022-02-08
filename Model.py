# создание бд
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
# взаимодействие с бд
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import View
#БД
#на данном этапе заранее создана пустая БД без таблиц итд


engine = create_engine("postgresql+psycopg2://postgres:Delovem!1@localhost/4months")
engine.connect()

Base = declarative_base()

class DBproduct(Base):
    __tablename__ = 'ProductsTable'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)

Base.metadata.create_all(engine)



#для вывода таблицы БД в ГУИ

#РАБОЧИЙ КЛАСС
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
        session = Session(bind=engine)
        prod = DBproduct(
            title=self.name,
            price=self.price,
            count=self.count
        )

        session.add(prod)
        session.commit()

    def delete_product(self):
        '''удаление товара из списка'''
        pass

    def minprice(self):
        '''возвращает товар с минимальной ценой'''
        pass

    def maxprice(self):
        '''возвращает товар с максимальцой ценой'''
        pass


NewProd = Product(View.create_entry)


#Импорт файла





if __name__ == "__main__":
    Velociped = Product("Велосипед", 500, 4)
    Cow = Product("Корова", 3000, 6)

print(Cow.product_info())
Cow.add_product()